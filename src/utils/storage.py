from azure.core.exceptions import ResourceNotFoundError
from azure.data.tables import TableServiceClient, TableClient
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient
import logging

def connect_to_storage_queue(url, queue_name) -> QueueClient | None:
    try:
        credential = DefaultAzureCredential()
        queue_client = QueueClient(
            account_url=url,
            queue_name=queue_name,
            credential=credential
        )
        logging.info('Connected to queue.')
    except Exception as e:
        logging.error(f'Failed to connect to storage queue: {e}')
        return None
    
    return queue_client

def connect_to_table_storage(endpoint, table_name: str) -> TableClient | None:
    try:
        credential = DefaultAzureCredential()
        service_client = TableServiceClient(
            endpoint=endpoint,
            credential=credential
        )
    except Exception as e:
        logging.error(f'Failed to connect to Table Storage service: {e}')
        return None
    
    if table_name in [table.name for table in service_client.list_tables()]:
        table_client = service_client.get_table_client(table_name=table_name)
        logging.info(f'Table "{table_name}" found.')
    else:
        logging.error(f'Table "{table_name}" not found.')
        return None
    
    return table_client

def find_repeat_sn(table_client: TableClient, product: str, serial_number: str) -> bool:
    try:
        query_filter = f"Product eq '{product}' and SerialNumber eq {serial_number}"
        paged_entities = table_client.query_entities(query_filter)
        logging.error(f'Repeat SN found. Partition Key: {product}, Row Key:{serial_number}')
        if paged_entities.next:
            return True
    except ResourceNotFoundError:
        logging.info(f'No repeat found. Saving new SN and sending LC command.')
    return False