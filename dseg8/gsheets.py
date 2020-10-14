import os
from dotenv import load_dotenv
# import pickle
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

load_dotenv()

# https://docs.google.com/spreadsheets/d/1UfxANlKkNRiF1rh1o6_kY8Z2fGKTsY_8_bust_ETqso/edit?usp=sharing

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./credentials.json"

SHEET_FRIENDS = "friends"
SHEET_PERSONAL_SUPPLEMENTS = "personal_supplement"
SHEET_FORM_RESPONSE = "FormResponse"
SHEET_TEST = "test_sheet"


class GoogleSheet():
    __GSHEET_ID = os.getenv('GSHEET_ID')
    __GSHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # __GMAP_KEY = os.getenv("GMAP_KEY")
    __FRIENDS_RANGE = 'friends'

    def __init__(self, sheet_name=""):
        service = build('sheets', 'v4', developerKey=os.getenv('GMAP_ID'))
        self.__GOOGLESHEET = service.spreadsheets()
        self.__FRIENDS_RANGE = sheet_name
        result = self.__GOOGLESHEET.values().get(
            spreadsheetId=self.__GSHEET_ID, range=self.__FRIENDS_RANGE).execute()
        # print(result)
        data = result.get('values', [])
        self.df = pd.DataFrame(data[1:], columns=data[0])

    def save(self):
        friends_list = self.df.T.reset_index().values.T.tolist()
        print(friends_list)
        self.__GOOGLESHEET.values().update(
            spreadsheetId=self.__GSHEET_ID,
            range=self.__FRIENDS_RANGE,
            valueInputOption="RAW",
            body={"values": friends_list}).execute()

        # def __get_sheet():
        #     global __googlesheet
        #     if __googlesheet is None:
        #         # creds = None
        #         # if os.path.exists('token.pickle'):
        #         #     with open('token.pickle', 'rb') as token:
        #         #         creds = pickle.load(token)
        #         # if not creds or not creds.valid:
        #         #     if creds and creds.expired and creds.refresh_token:
        #         #         creds.refresh(Request())
        #         #     else:
        #         #         flow = InstalledAppFlow.from_client_secrets_file(
        #         #             'credentials.json', GSHEET_SCOPES)
        #         #         creds = flow.run_local_server(port=0)
        #         #     with open('token.pickle', 'wb') as token:
        #         #         pickle.dump(creds, token)

        #         # service = build('sheets', 'v4', credentials=creds)
        #         service = build('sheets', 'v4', developerKey=__GMAP_KEY)
        #         __googlesheet = service.spreadsheets()

        #     return __googlesheet


def read_friends():
    sheet = __get_sheet()
    RANGE = __friends_range
    result = sheet.values().get(
        spreadsheetId=__GSHEET_ID, range=RANGE).execute()
    rows = result.get('values', [])
    return rows


def write_friends(id, name):
    sheet = __get_sheet()
    rows = read_friends()
    rows.append([id, name])
    result = sheet.values().update(
        spreadsheetId=__GSHEET_ID,
        range="friends!a2:d",
        valueInputOption="RAW",
        body={"values": rows}).execute()
    return result
