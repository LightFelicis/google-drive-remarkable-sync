from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]

def load_token():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def search_for_folder_with_name(service_driver, name):
    page_token = None
    query = "mimeType = 'application/vnd.google-apps.folder' and " + "name = '" + name + "'"
    while True:
        response = service_driver.files().list(q = query,
                                               pageToken=page_token).execute()
        for file in response.get('files', []):
            return (True, file.get('id'))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return (False, None)


def main():
    creds = load_token()
    service = build('drive', 'v3', credentials=creds)
    print("Welcome to Google drive sync remarkable tool! Please write down the name of the folder with your books:")
    folder_name = input()
    found, folder_id = search_for_folder_with_name(service, folder_name)
    if not found:
        print("Folder with name", folder_name, " was not found, try again...")
        return
    else:
        print("Gotcha! Your folder has id =", folder_id)

if __name__ == '__main__':
    main()
