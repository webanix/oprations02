import azure.functions as func
import logging
import json
from datetime import datetime, timedelta

app = func.FunctionApp()

# ================== MAIN IOT HUB TRIGGER ==================

@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="iothub-ehub",  # IoT Hub built-in event hub
    connection="IOTHUB_CONNECTION"
)
@app.blob_output(
    arg_name="outputBlob",
    path="falcondata01/{rand-guid}.json",
    connection="AzureWebJobsStorage",
)
def iot_hub_trigger(event: func.EventHubEvent, outputBlob: func.Out[str]):
    msg = event.get_body().decode()

    full_event = {
        "body": msg,
        "enqueued_time": event.enqueued_time.isoformat(),
    }

    logging.info(f"IoT Hub message received: {full_event}")

    outputBlob.set(json.dumps(full_event))


# ================== HELPERS (SAFE — NO HEAVY IMPORTS) ==================

def wait_my_turn(context):
    from settings import RECHECK_OPS1_Q_TIME  # import ONLY when needed

    queue = yield context.call_activity('get_queue_msgs', '2')
    next_in_line = queue[0]

    while next_in_line != context.instance_id:
        execute_datetime = context.current_utc_datetime + timedelta(
            seconds=RECHECK_OPS1_Q_TIME
        )
        yield context.create_timer(execute_datetime)

        queue = yield context.call_activity('get_queue_msgs', '2')
        next_in_line = queue[0]

    return True


def is_valid_message(message) -> bool:
    if 'SN' not in message:
        return False
    if 'topic' not in message:
        return False
    if 'data' not in message:
        return False
    return True

