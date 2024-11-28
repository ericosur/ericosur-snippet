#!/usr/bin/env python3
# coding: utf-8

'''
use api.myip.com to get current public ip
and use ip-api.com to get location of such ip
'''

import argparse
import json
import requests

DEBUG = True
USE_RICH = False
try:
    from rich import print_json
    from rich import print as rprint
    from rich.console import Console
    USE_RICH = True
except ImportError:
    print('suggest: use __pip install rich__')

def logd(*args, **wargs) -> None:
    ''' logd '''
    if DEBUG:
        if USE_RICH:
            rprint(*args, **wargs)
        else:
            print(*args, **wargs)

class Main():
    ''' main '''
    def __init__(self):
        self.args = None
        self.mk_parser()

    @classmethod
    def run(cls) -> None:
        ''' run '''
        obj = cls()
        obj.action()

    def mk_parser(self) -> None:
        ''' make parser '''
        parser = argparse.ArgumentParser(description='use ip-api.com to query IP')
        parser.add_argument("ips", metavar='str', type=str, nargs='*',
            help="specify IP")
        parser.add_argument("-r", "--rich", action='store_true', default=False,
            help='view in rich text')
        self.args = parser.parse_args()

    def print_data(self, data) -> None:
        ''' print json if rich is available '''
        d = json.dumps(data)
        if USE_RICH and self.args.rich:
            print_json(d)
        else:
            print(d)

    def get_current_ip(self) -> str:
        ''' use this to get myip '''
        url = 'https://api.myip.com'
        try:
            r = requests.get(url, timeout=5.0)
            logd('get_current_ip: url:', r.url)
            data = r.json()
            print("returned:")
            self.print_data(data)
            ip = data['ip']
            return ip
        except requests.exceptions.ConnectionError as e:
            rprint("[red] failed to connect:", e)
            return None

    def get_ip_info(self, ip:str) -> None:
        ''' use this to get IP location and related data '''
        if ip is None:
            rprint('[red]ip was not specified')
            return
        try:
            iploc = f'http://ip-api.com/json/{ip}'
            r = requests.get(iploc, timeout=5.0)
            print(f'get_ip_info: {r.url=}')
            print("returned:")
            self.print_data(r.json())
        except requests.exceptions.ConnectionError as e:
            rprint("[red] failed to connect:", e)

    def action(self) -> None:
        ''' action '''
        if not self.args.ips:
            logd("will get current ip...")
            curr_ip = self.get_current_ip()
            #logd(f'current ip: {ret}')
            self.get_ip_info(curr_ip)
            return
        for i in self.args.ips:
            logd(f'query: {i}')
            self.get_ip_info(i)

def main():
    ''' main '''
    Main.run()

if __name__ == '__main__':
    main()
