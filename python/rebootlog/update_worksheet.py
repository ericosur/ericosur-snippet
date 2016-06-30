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
import getopt, sys

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


def usage():
    print("--auth, -a: auth json path")
    print("--key, -k: spreadsheet key path")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:k:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    auth_json_path = 'auth.json'
    spreadsheet_key_path = 'spreadsheet_key'
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


if __name__ == "__main__":
    main()

