#!/usr/bin/env python3
# coding: utf-8

'''
sick number

here sick means:
    ns (int) -> ns (float) -> ns (hex) -> show as (int)

'''

import math
import struct
import time
import logging
from datetime import datetime
from sysconfig import get_platform
#from nothing import do_nothing

logi = logging.info
logd = logging.debug
loge = logging.error

def is_linux() -> bool:
    ''' return true if linux '''
    p = get_platform()
    logi(f'platform: {p}')
    return "linux" in p

def float_to_hex(f: float) -> str:
    """Converts a float value to a hexadecimal string.
    Args:
        f: The float value to convert.
    Returns:
        A hexadecimal string representing the float value.
    """
    # Pack the float into a 4-byte binary string
    binary_data = struct.pack("d", f)
    # Convert the binary string to hexadecimal
    hex_string = binary_data.hex()
    return hex_string

def sick_to_ns(sick: int) -> int:
    ''' sick to datetime '''
    if not isinstance(sick, int):
        raise ValueError('sick should be an int')
    logd(f'----- sick_to_ns({sick}) -----')
    hex_string = normalize_hex_str(hex(sick))
    logd(f'  {hex_string=}, {len(hex_string)=}')
    float_val = struct.unpack("d", bytes.fromhex(hex_string))[0]
    logd(f'  {float_val=}')
    ns_val = int(float_val)
    logd(f'  {ns_val=}')
    return ns_val

def normalize_hex_str(the_hexstr: str) -> str:
    ''' the hex str should be [0-9a-fA-F]{16}, without "0x" prefix '''
    #logd(f'----- normalize_hex_str({the_hexstr} ({len(the_hexstr)})) -----')
    tmp = ''
    if the_hexstr.index('0x') >= 0:
        tmp = the_hexstr[2:]
    else:
        tmp = the_hexstr
    lstr = len(tmp)
    if lstr % 8 != 0:
        pad = ''
        for _ in range(8-(lstr%8)):
            pad += '0'
        tmp = pad + tmp
    return tmp

def sick_to_datetime(val: int) -> None | datetime:
    ''' sick to datetime '''
    if not isinstance(val, int):
        raise ValueError
    logd(f'----- sick_to_datetime({val}) -----')
    hex_string = normalize_hex_str(hex(val))
    logd(f'  {hex_string=}, {len(hex_string)=}')
    float_val = struct.unpack("d", bytes.fromhex(hex_string))[0]
    logd(f'  {float_val=}')
    if isinstance(float_val, float):
        if float_val < 0.0:
            loge('ERROR: smaller than zero')
            return None
        the_log10 = math.log10(float_val)
        if 18.0 <= the_log10 < 19.0:  # in the range
            #logd('  log10:', math.log10(float_val))
            pass
        else:
            loge('ERROR: out of range')
            return None

    int_val = int(float_val)
    logd(f'  {int_val=}')
    str_val = str(int_val)
    # str_val represents in ns, will strip the last 9 digits
    keep_len = len(str_val) - 9
    str_val = str_val[:keep_len]
    logd(f'  {str_val=}')
    dt = datetime.fromtimestamp(int(str_val))
    return dt

def get_sick_from_ns(ns_val: int) -> int:
    ''' get_sick_from_ns '''
    logd(f'----- get_sick_from_ns {ns_val=} -----')
    ns_float_hex = float_to_hex(float(ns_val))
    #logd(f'  {ns_float_hex=}')
    sick = int(ns_float_hex, 16)
    #logd(f'   {sick=}')
    return sick

# pylint: disable=no-member
def sick_integer2(ns_val: int) -> None:
    ''' given time_ns '''
    if not is_linux():
        loge("sick_integer2: only for linux...")
        return
    logd('----- sick_integer2 -----')
    # get the resolution of realtime clock
    resolution = time.clock_getres(time.CLOCK_REALTIME)
    logd(f'clock {time.CLOCK_REALTIME=} resolution: {resolution}')
    si = float(ns_val * resolution)
    lsi = len(str(si))
    logd(f'repeat NA, len={lsi:2d}, {si=}')
    float_val = float_to_hex(si)
    logd(f'{len(float_val)=}, {float_val=}')

def datetime_to_sick(dt: datetime) -> int:
    ''' given datetime to sick number '''
    ts = int(dt.timestamp()*1e9)
    lts = len(str(ts))
    # should be 19 digits
    assert lts == 19
    return ts

if __name__ == "__main__":
    print("provides functions only")
    print("DO NOT run this script...")
