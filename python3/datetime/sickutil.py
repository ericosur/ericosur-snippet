#!/usr/bin/python3
# coding: utf-8

'''
sick number

here sick means:
    ns (int) -> ns (float) -> ns (hex) -> show as (int)

'''

import math
import struct
import sys
import time
from datetime import datetime

VERBOSE = False
ERROR = True

def logv(*args, **wargs):
    ''' logv '''
    if VERBOSE:
        print(*args, **wargs)

def loge(*args, **wargs):
    ''' loge '''
    if ERROR:
        print(*args, **wargs, file=sys.stderr)

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

def sick_to_ns(sick):
    ''' sick to datetime '''
    if not isinstance(sick, int):
        raise ValueError('sick should be an int')
    logv(f'----- sick_to_ns({sick}) -----')
    hex_string = normalize_hex_str(hex(sick))
    logv(f'  {hex_string=}, {len(hex_string)=}')
    float_val = struct.unpack("d", bytes.fromhex(hex_string))[0]
    logv(f'  {float_val=}')
    ns_val = int(float_val)
    logv(f'  {ns_val=}')
    return ns_val

def normalize_hex_str(the_hexstr):
    ''' the hex str should be [0-9a-fA-F]{16}, without "0x" prefix '''
    #logv(f'----- normalize_hex_str({the_hexstr} ({len(the_hexstr)})) -----')
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

def sick_to_datetime(val):
    ''' sick to datetime '''
    if not isinstance(val, int):
        raise ValueError
    logv(f'----- sick_to_datetime({val}) -----')
    hex_string = normalize_hex_str(hex(val))
    logv(f'  {hex_string=}, {len(hex_string)=}')
    float_val = struct.unpack("d", bytes.fromhex(hex_string))[0]
    logv(f'  {float_val=}')
    if isinstance(float_val, float):
        if float_val < 0.0:
            loge('ERROR: smaller than zero')
            return None
        the_log10 = math.log10(float_val)
        if 18.0 <= the_log10 < 19.0:  # in the range
            #logv('  log10:', math.log10(float_val))
            pass
        else:
            loge('ERROR: out of range')
            return None

    int_val = int(float_val)
    logv(f'  {int_val=}')
    str_val = str(int_val)
    # str_val represents in ns, will strip the last 9 digits
    keep_len = len(str_val) - 9
    str_val = str_val[:keep_len]
    logv(f'  {str_val=}')
    dt = datetime.fromtimestamp(int(str_val))
    return dt

def get_sick_from_ns(ns_val):
    ''' get_sick_from_ns '''
    logv(f'----- get_sick_from_ns {ns_val=} -----')
    ns_float_hex = float_to_hex(float(ns_val))
    #logv(f'  {ns_float_hex=}')
    sick = int(ns_float_hex, 16)
    #logv(f'   {sick=}')
    return sick

def sick_integer2(ns_val):
    ''' given time_ns '''
    logv('----- sick_integer2 -----')
    # get the resolution of realtime clock
    resolution = time.clock_getres(time.CLOCK_REALTIME)
    logv(f'clock {time.CLOCK_REALTIME=} resolution: {resolution}')
    si = float(ns_val * resolution)
    lsi = len(str(si))
    logv(f'repeat NA, len={lsi:2d}, {si=}')
    float_val = float_to_hex(si)
    logv(f'{len(float_val)=}, {float_val=}')

def datetime_to_sick(dt):
    ''' given datetime to sick number '''
    ts = int(dt.timestamp()*1e9)
    lts = len(str(ts))
    # should be 19 digits
    assert lts == 19
    return ts
