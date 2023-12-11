#!/usr/bin/env python3
# coding: utf-8

''' try to oauth with gspread '''

import os
import sys

try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
    print('ImportError')
    sys.exit(1)


def auth_gss_client(path, scopes):
    ''' auth gss client '''
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
    return gspread.authorize(credentials)

def main():
    ''' main '''
    home = os.environ['HOME']
    auth_json_path = home + '/Private/auth.json'
    gss_scopes = ['https://spreadsheets.google.com/feeds']
    gss_client = auth_gss_client(auth_json_path, gss_scopes)
    print(gss_client)

if __name__ == '__main__':
    main()
