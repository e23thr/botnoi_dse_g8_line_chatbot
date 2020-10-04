import os
from dotenv import load_dotenv
# import pickle
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

load_dotenv()

# for test
#  https://docs.google.com/spreadsheets/d/1rjNddk8756QW0Rl3mARTCDXzagSWQ3SDjV1iSIPtFg0/edit#gid=0
# for live
# https://docs.google.com/spreadsheets/d/1UfxANlKkNRiF1rh1o6_kY8Z2fGKTsY_8_bust_ETqso/edit?usp=sharing

# __googlesheet = None

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./credentials.json"


class GoogleSheet():
    __GSHEET_ID = os.getenv('GSHEET_ID')
    __GSHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # __GMAP_KEY = os.getenv("GMAP_KEY")
    __FRIENDS_RANGE = 'friends'

    def __init__(self):
        service = build('sheets', 'v4', developerKey=os.getenv('GMAP_ID'))
        self.__GOOGLESHEET = service.spreadsheets()

    def read_friends(self):
        result = self.__GOOGLESHEET.values().get(
            spreadsheetId=self.__GSHEET_ID, range=self.__FRIENDS_RANGE).execute()
        data = result.get('values', [])
        self.friends_pd = pd.DataFrame(data[1:], columns=data[0])
        return self.friends_pd

    def write_friends(self):
        friends_list = self.friends_pd.T.reset_index().values.T.tolist()
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
