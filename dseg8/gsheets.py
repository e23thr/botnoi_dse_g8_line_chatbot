import os
from dotenv import load_dotenv
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

load_dotenv()

#  https://docs.google.com/spreadsheets/d/1rjNddk8756QW0Rl3mARTCDXzagSWQ3SDjV1iSIPtFg0/edit#gid=0
GSHEET_ID = os.getenv('GSHEET_ID')
GSHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

friends_range = 'friends!a2:b'

googlesheet = None


def get_sheet():
    global googlesheet
    if googlesheet is None:
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', GSHEET_SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)
        googlesheet = service.spreadsheets()

    return googlesheet


def read_friends():
    sheet = get_sheet()
    RANGE = "friends!a2:d"
    result = sheet.values().get(
        spreadsheetId=GSHEET_ID, range=RANGE).execute()
    rows = result.get('values', [])
    return rows


def write_friends(id, name):
    sheet = get_sheet()
    rows = read_friends()
    rows.append([id, name])
    result = sheet.values().update(
        spreadsheetId=GSHEET_ID,
        range="friends!a2:d",
        valueInputOption="RAW",
        body={"values": rows}).execute()
    return result
