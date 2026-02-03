from typing import TypedDict, Any

class TestDataMessage(TypedDict):
    topic: str
    SN: str
    data: dict[str, Any]

class Ops1ResponseData(TypedDict):
    status: str
    data: Any

class Ops1ReportData(TypedDict):
    type: str
    product: str
    id: str
    serial_number: str
    passed: bool

class Ops1SaveData(TypedDict):
    product: str
    report_id: int
    vpid: int
    value: int | float | str
    step: int