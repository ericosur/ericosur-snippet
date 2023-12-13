#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
update.py

use google drive api, Google cloud platform to insert data into specified spreadsheet

ip addr show eth0 |grep -w inet

'''

import getopt
# update google spread sheet
import os
import socket
import sys
import time

from myiputil import get_extip, get_iface_ip, get_ssid

try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError as e:
    print('ImportError:', e)
    sys.exit(-1)

# oauth2
def auth_gss_client(path, scopes):
    ''' auth_gss_client '''
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
    return None


def update_sheet(gss_client, key, **kwargs):
    ''' update_sheet '''
    # host, date, eth0, wlan0, ssid, extip
    try:
        wks = gss_client.open_by_key(key)
        sheet = wks.sheet1
        sheet.insert_row([kwargs['date'], kwargs['host'], kwargs['eth0'],
                          kwargs['wlan0'], kwargs['ssid'], kwargs['extip']], 2)
    except gspread.GSpreadException as err:
        print("gspread exception!", err)


def usage():
    ''' usage '''
    print("--auth, -a: auth json path")
    print("--key, -k: spreadsheet key path")

def main():
    ''' main '''
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "ha:k:", ["help", "auth=", "key="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    home = os.environ.get('HOME')
    auth_json_path = home + '/Private/auth.json'
    spreadsheet_key_path = home + '/Private/spreadsheet_key'
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-a", "--auth"):
            auth_json_path = a
        elif o in ("-k", "--key"):
            spreadsheet_key_path = a
        else:
            assert False, "unhandled option"

    print('auth:' + auth_json_path)
    print('spread:' + spreadsheet_key_path)

    gss_scopes = ['https://spreadsheets.google.com/feeds']
    gss_client = auth_gss_client(auth_json_path, gss_scopes)

    kwargs = {}
    try:
        kwargs['host'] = socket.gethostname()
        kwargs['date'] = time.strftime("%c")
        kwargs['eth0'] = get_iface_ip("eth0")
        kwargs['wlan0'] = get_iface_ip("wlan0")
        kwargs['ssid'] = get_ssid()
        kwargs['extip'] = get_extip()
        with open(spreadsheet_key_path, encoding='UTF-8') as f:
            spreadsheet_key = f.read().strip()
            update_sheet(gss_client, spreadsheet_key, **kwargs)
    except IOError:
        print('IOError')


if __name__ == "__main__":
    main()
