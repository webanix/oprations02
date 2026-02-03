import os

# Operations1 API Settings
TENANT = os.getenv('OP1_TENANT', '')
TOKEN = os.getenv('OP1_TOKEN', '')
BASE_URL = os.getenv('OPS1_API_BASE_URL', 'https://api.operations1.app/tenants')

DEFAULT_RETRY_TIME = 5 # seconds
MAX_API_RETRIES = 5
SN_IID = 274
INSPECTION_PROD_TYPE_IID = 306
PROD_TYPE_KEY = 'Produkt Typ / Product Type'
TEST_TYPE_KEY = 'Test Type'

# Azure Storage Resource Settings
OPS1_API_Q_NAME = os.getenv('OPS1_Q_NAME', 'ops1-api-queue')
OPS1_API_Q_URL = os.getenv('OPS1_Q_URL', 'https://sttestdatasvcprod01.queue.core.windows.net')
TABLE_STORAGE_URL = os.getenv('TABLE_STORAGE_URL', 'https://sttestdatasvcprod01.table.core.windows.net')
PERF_REPORT_TABLE = os.getenv('REPORT_CACHE_NAME', 'O1PerformanceReports')
FINAL_INSP_REPORT_TABLE = os.getenv('FINAL_INSP_REPORT_CACHE', 'O1FinalInspectionReports')

RECHECK_OPS1_Q_TIME = 10 # seconds

# Product settings
PRODUCT_SETTINGS = {
    "rook2": {
        'performance': {
            'supported': True, 
            "product_classifier_id": 247,
            "stepPosition": 2, 
            "vpids": {
                "SN": 15390, 
                "PD": 15429, 
                "PWR": 15430, 
                "SCFM": 15431, 
                "TA": 15432, 
                "ST": 15433, 
                "AV": 15434, 
                "RV": 15435, 
                "Hz": 0, 
            }, 
        }, 
        'final_insp': {
            'supported': True, 
            'prefix': 'BL', 
            'pn': 'PN.000.00000', 
        }, 
    }, 
    "falcon": {
        'performance': {
            'supported': True, 
            "product_classifier_id": 245,
            "stepPosition": 2, 
            "vpids": {
                "SN": 9728,
                "RPM": 15533, 
                "PWR": 15534, 
                "A": 15535, 
                "TA": 15586, 
                "ST": 15537, 
                "V": 9735, 
                "RV1": 15513,  
                "AV1": 15514, 
                "RV2": 15515, 
                "AV2": 15516, 
                "RV3": 15517, 
                "AV3": 15518, 
                "RV4": 15519, 
                "AV4": 15520, 
                "RV5": 15521, 
                "AV5": 15522, 
                "PG": 0, 
            }, 
        }, 
        'final_insp': {
            'supported': True, 
            'prefix': 'BL', 
            'pn': 'PN.000.00000', 
        }, 
    }, 
    "miniakb": {
        'performance': {
            'supported': True, 
            "product_classifier_id": 246,
            "stepPosition": 2, 
            "vpids": {
                "SN": 10146, 
                "ST": 15625, 
                "Test Press": 1, 
                "Press Decay": 15626, 
                "Pressure": 10290, 
                "Leak Result": 1, 
                "AV": 16116, 
                "RV": 16117, 
                "TA": 15630, 
                "PWR": 10305, 
                "AMPS": 10292, 
                "RPM": 10291, 
            }, 
        }, 
        'final_insp': {
            'supported': True, 
            'prefix': 'BL', 
            'pn': 'PN.000.00000', 
        }, 
    }, 
    "abl": {
        'performance': {
            'supported': False, 
        }, 
        'final_insp': {
            'supported': False, 
        }, 
    }, 
}