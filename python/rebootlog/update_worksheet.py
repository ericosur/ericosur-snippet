'''
update.py

use google drive api, Google cloud platform to insert data into specified spreadsheet

ip addr show eth0 |grep -w inet

'''

# update google spread sheet
import gspread
import time
import socket
import myutil

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


def update_sheet(gss_client, key, host, date, eth0, wlan0, ssid, extip):
    try:
        wks = gss_client.open_by_key(key)
        sheet = wks.sheet1
        sheet.insert_row([date, host, eth0, wlan0, ssid, extip], 2)
    except:
        print("unexpect error at update_sheet()");


# oauth2
if __name__ == "__main__":
    auth_json_path = '/home/ericosur/Private/auth.json'
    spreadsheet_key_path = '/home/ericosur/Private/spreadsheet_key'
    gss_scopes = ['https://spreadsheets.google.com/feeds']

    gss_client = auth_gss_client(auth_json_path, gss_scopes)

    today = time.strftime("%c")
    host = socket.gethostname()
    eth0 = myutil.get_iface_ip("eth0")
    wlan0 = myutil.get_iface_ip("wlan0")
    ssid = myutil.get_ssid()
    extip = myutil.get_extip()

    try:
        f = open(spreadsheet_key_path)
    except IOError:
        print('IOError')
    else:
        with f:
            spreadsheet_key = f.read().strip()
            update_sheet(gss_client, spreadsheet_key,
                host, today, eth0, wlan0, ssid, extip)
