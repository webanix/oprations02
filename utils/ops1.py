from settings import (
    TOKEN,
    TENANT, 
    BASE_URL, 
    SN_IID, 
    MAX_API_RETRIES, 
    DEFAULT_RETRY_TIME,
    PRODUCT_SETTINGS
)
import logging
import requests
import time
from typing import Any
from utils.types import Ops1ResponseData, Ops1SaveData

def _get_headers(api_version='2025-04-01') -> dict[str, str]:
    return {
        "accept": "application/json",
        "accept-version": api_version,
        "content-type": "application/json",
        "authorization": f"Bearer {TOKEN}"
    }

# def get_document_id(product: str) -> Ops1ResponseData:
#     product_classifier_id = PRODUCT_SETTINGS[product]['ops1'].get('product_classifier_id', -1)
#     url = BASE_URL + '/' + TENANT + f'/documents?lang=en&pageSize=200&pageIndex=0&classCharacteristicIds={product_classifier_id}'
#     headers = _get_headers()
    
#     for _ in range(MAX_API_RETRIES):
#         try: 
#             response = requests.get(url, headers=headers)

#             # Retry if rate limit hit
#             if response.status_code == 429:
#                 retry_after = response.headers.get('retry-after', DEFAULT_RETRY_TIME)
#                 logging.info(f'Rate limited. Retrying after {retry_after} seconds...')
#                 time.sleep(int(retry_after))
#                 continue
#         except Exception as e:
#             logging.error(f'Error getting documents for product classifier id {product_classifier_id}: {e}')
#             return {'status': 'error', 'data': None}

#         break

#     documents = response.json().get('items', [])
#     if len(documents) == 0:
#         logging.error(f'No documents found for product {product} (product_classifier_id: {product_classifier_id})')
#         return {'status': 'error', 'data': None}
    
#     doc_id = documents[-1]['id']
#     return {'status': 'success', 'data': doc_id}

def create_report(doc_id: str) -> Ops1ResponseData:
    url = BASE_URL + '/' + TENANT + '/reports'
    headers = _get_headers()
    payload = {
        'documentId': doc_id, 
    }
    
    for _ in range(MAX_API_RETRIES):
        try: 
            response = requests.post(url, headers=headers, json=payload)

            # Retry if rate limit hit
            if response.status_code == 429:
                retry_after = response.headers.get('retry-after', DEFAULT_RETRY_TIME)
                logging.info(f'Rate limited. Retrying after {retry_after} seconds...')
                time.sleep(int(retry_after))
                continue
            response.raise_for_status()
        except Exception as e:
            logging.error(f'Error creating report from document id {doc_id}: {e}')
            return {'status': 'error', 'data': None}
        break
    
    report = response.json()
    report_id = report['id']
    return {'status': 'success', 'data': report_id}

# def update_report(data: Ops1SaveData) -> Ops1ResponseData:
#     report_id = data['report_id']
#     url = BASE_URL + '/' + TENANT + f'/reports/{report_id}/interaction-values/interaction-version-persistent-id'
#     headers = _get_headers()

#     payload = {
#         "value": str(data['value']), 
#         "stepPosition": data['step'], 
#         "interactionVersionPersistentId": data['vpid'], 
#     }

#     for _ in range(MAX_API_RETRIES):
#         try:
#             response = requests.put(url, json=payload, headers=headers)

#             # Retry if rate limit hit
#             if response.status_code == 429:
#                 retry_after = response.headers.get('retry-after', DEFAULT_RETRY_TIME)
#                 logging.info(f'Rate limited. Retrying after {retry_after} seconds...')
#                 time.sleep(int(retry_after))
#                 continue
#         except Exception as e:
#                 logging.error(f'Error updating report {report_id}: {e}')
#                 return {'status': 'error', 'data': None}
#         break

#     logging.info(f'Successfully updated report.')
#     return {'status': 'success', 'data': None}

# def get_latest_reports(states=['done'], pages=1) -> Ops1ResponseData:
#     states_adder = ''
#     for state in states:
#         states_adder += f'&states={state}'
#     url = BASE_URL + '/' + TENANT + f'/reports?pageSize=40&orderBy=id&direction=DESC{states_adder}'
#     headers = _get_headers()
    
#     report_ids = []
#     for page in range(pages):
#         page_adder = f'&pageIndex={page}'
#         for _ in range(MAX_API_RETRIES):
#             try:
#                 response = requests.get(url+page_adder, headers=headers)

#                 # Retry if rate limit hit
#                 if response.status_code == 429:
#                     retry_after = response.headers.get('retry-after', DEFAULT_RETRY_TIME)
#                     logging.info(f'Rate limited. Retrying after {retry_after} seconds...')
#                     time.sleep(int(retry_after))
#                     continue
#                 break
#             except Exception as e:
#                 logging.error(f'Error getting last 200 reports: {e}')
#                 return {'status': 'error', 'data': None}
        
#         try:
#             reports = response.json()
#         except Exception as e:
#             logging.error(f'Error extracting JSON from Ops1 GET reports call: {e}')
#             return {'status': 'error', 'data': None}

#         if 'items' in reports:
#             report_ids += [report['id'] for report in reports['items']]
#             logging.info(f'Retrieved open reports.')
#         else:
#             logging.error('Max retries reached or no reports found')

#     return {'status': 'success', 'data': report_ids}

# def get_interactions(report_id: int) -> Ops1ResponseData:
#     sn_iid_url_adder = ''
#     if SN_IID != 0:
#         sn_iid_url_adder = f'&interactionTagIds={SN_IID}'

#     url = BASE_URL + '/' + TENANT + f'/reports/{report_id}/interaction-values?pageSize=200&pageIndex=0{sn_iid_url_adder}'
#     headers = _get_headers()

#     for _ in range(MAX_API_RETRIES):
#         try:
#             response = requests.get(url, headers=headers)

#             # Retry if rate limit hit
#             if response.status_code == 429:
#                 retry_after = response.headers.get('retry-after', DEFAULT_RETRY_TIME)
#                 logging.info(f'Rate limited. Retrying after {retry_after} seconds...')
#                 time.sleep(int(retry_after))
#                 continue
#             break
#         except Exception as e:
#                 logging.error(f'Error getting interactions for report {report_id}: {e}')
#                 return {'status': 'error', 'data': None}
    
#     interaction_data = response.json()
#     interactions = []
#     if 'items' in interaction_data:
#         interactions = interaction_data['items']

#     return {'status': 'success', 'data': interactions}