#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007 朱昱任 (Yuren Ju) <yurenju -AT- gmail.com>
# Released under GNU General Public License


import os

version = '0.1'

def main():
    fin, fout = os.popen2("zenity --width=400 --height=230 --list --title='切換顯示器' --column='模式' --column='敘述' LCD '只用 LCD' both 'LCD, 外接螢幕都開啟'")
    selected_mode = fout.read().strip()
    
    if selected_mode == "both":
        os.system("xrandr --output LVDS --output VGA-0 --mode 1024x768 --auto")
    elif selected_mode == "LCD":
        os.system("xrandr --output LVDS --mode 1024x768 --output VGA-0 --off")

if __name__ == "__main__":
    main()
