import logging
from office365.runtime.auth.client_credential import ClientCredential
from office365.runtime.client_request_exception import ClientRequestException
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import os

CLIENT_ID = os.getenv('O365_CLIENT', '')
CLIENT_SECRET = os.getenv('O365_SECRET', '')
# BASE_URL = 'https://idexonline.sharepoint.com/:f:/r/sites/AirtechJDE'

# def connect_to_o365() -> ClientContext | None:
#     credentials = ClientCredential(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
#     logging.info(f'{CLIENT_ID}, {CLIENT_SECRET}, {credentials}')
#     client_context = ClientContext(BASE_URL).with_credentials(credentials)
#     try:
#         site = client_context.web.get().execute_query()
#     except ClientRequestException as e:
#         if e.response.status_code == 401:
#             logging.error(f"code: {e.response.status_code}, message: Authentication failed: Invalid credentials.")
#             return None
#         if e.response.status_code == 403:
#             logging.error(f"code: {e.response.status_code}, message: Access denied: Check permissions.")
#             return None
#         else:
#             logging.error(f"code: {e.response.status_code}, message: Failed to connect.")
#             return None
#     except Exception as e:
#         logging.error(f"code: 0, message: Unexpected error occured: {e}")
#         return None
    
#     logging.info(f"code: {201}, message: Connection verified. Site title: {site.properties['Title']}")
#     return client_context

# def save_lc_info(client_context: ClientContext, file_name: str, file_content: str) -> File | None:
#     DROP_FOLDER = '/Shared%20Documents/Integrations/Integration%20File%20Drops/Lean%20Completions'
#     target_folder = client_context.web.get_folder_by_server_relative_url(DROP_FOLDER)
#     try:
#         file = target_folder.upload_file(file_name, file_content)
#     except Exception as e:
#         logging.error(e)
#         return None
#     return file