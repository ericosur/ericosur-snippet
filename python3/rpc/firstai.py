#!/usr/bin/env python3
#coding: UTF-8

'''
using google AI studio
'''

import sys
from datetime import datetime, timezone

try:
    import google.generativeai as genai
except ImportError:
    print("ImportError: pip install google-generativeai")
    sys.exit()
from rich.console import Console

from rich import print as prt

sys.path.insert(0, "..")
sys.path.insert(0, "../..")
sys.path.insert(0, "python3")
from myutil import DefaultConfig, read_jsonfile


class Solution:
    ''' google ai studio '''
    conf = 'google-ai-studio.json'
    log = 'conversation.log'

    def __init__(self):
        self.console = Console()
        self._initial()

    def _initial(self):
        ''' init '''
        logd = self.console.log
        logd('init...')

        #logd = do_nothing
        cnfn = DefaultConfig(self.conf, debug=False).get_default_config()
        logd(cnfn)
        data = read_jsonfile(cnfn)
        apikey = data['apikey']
        #logd(apikey)
        genai.configure(api_key=apikey)
        logd('genai configured...')

    @classmethod
    def run(cls):
        ''' run me '''
        obj = cls()
        obj.action()

    def append_to_log(self, msg):
        ''' append to log'''
        logd = self.console.log
        logd("incoming msg...")
        with open(self.log, "at", encoding='utf-8') as flog:
            print(datetime.now(tz=timezone.utc), file=flog)
            print(msg, file=flog)

    def action(self):
        ''' action '''
        logd = self.console.log
        logd("action...")
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = "Write a story about a magic axe in less than 500 words. " \
            "The main character is male teenager. Please response in " \
            "Traditional Chinese."

        self.append_to_log(prompt)
        resp = model.generate_content(prompt)
        prt(resp.text)
        self.append_to_log(resp.text)
        logd('finished.')

def main():
    ''' main '''
    Solution.run()

if __name__ == "__main__":
    main()
