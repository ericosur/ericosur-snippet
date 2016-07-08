#!/usr/bin/env python

'''
uploadCsv.py

use google drive api, Google cloud platform to insert data into specified spreadsheet
'''

# update google spread sheet
import gspread
import time
import getopt, sys
import csv

# oauth2
def auth_gss_client(path, scopes):
    from oauth2client.service_account import ServiceAccountCredentials
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
        gs_client = gspread.authorize(credentials)
        return gs_client
    except ValueError:
        print("auth_gss_client: ValueError")
    except KeyError:
        print("auth_gss_client: KeyError")
    except gspread.GSpreadException:
        print("gspread exception!")


def update_sheet(gss_client, key, file):
    # gspread
    wks = gss_client.open_by_key(key)
    sheet = wks.get_worksheet(1)
    print('row count: ' + str(sheet.row_count))
    # get the cell at the last row
    last_time = sheet.cell(sheet.row_count, 1)
    # local csv
    print('file: ' + file)
    # local csv
    with open(file, newline='') as csvfile:
        sw = csv.reader(csvfile)
        for row in sw:
            # only timestamp is newer than last time append
            if row[0] > last_time.value:
                print("append: " + str(row))
                sheet.append_row(row)


def usage():
    print("--auth, -a: auth json path")
    print("--key, -k: spreadsheet key path")
    print("--file, -f: specified csv file to upload")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:k:f:",
            ["help", "auth=", "key=", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    auth_json_path = 'auth.json'
    spreadsheet_key_path = 'spreadsheet_key'
    csv_path = 'd.csv'

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-a", "--auth"):
            auth_json_path = a
        elif o in ("-k", "--key"):
            spreadsheet_key_path = a
        elif o in ("-f", "--file"):
            csv_path = a
        else:
            assert False, "unhandled option"

    print('auth:' + auth_json_path)
    print('spread:' + spreadsheet_key_path)

    gss_scopes = ['https://spreadsheets.google.com/feeds']
    gss_client = auth_gss_client(auth_json_path, gss_scopes)

    try:
        f = open(spreadsheet_key_path)
    except IOError:
        print('IOError')
    else:
        with f:
            spreadsheet_key = f.read().strip()
            update_sheet(gss_client, spreadsheet_key, csv_path)

if __name__ == "__main__":
    main()

