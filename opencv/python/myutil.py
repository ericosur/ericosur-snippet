import os
import json

__version__ = '0.0.1'

def read_jsonfile(fn):
    '''
    specify json filename and return whole json object
    '''
    print('load json from {}'.format(fn))
    if not os.path.exists(fn):
        print('file not found')
        return None
    # read from json file

    # method #1
#    with open(filename) as sec_file:
#        data = json.load(sec_file)

    # kiss method #2
    data = json.load(open(fn))

    return data

# in order not to break client scripts
def read_setting(fn):
    return read_jsonfile(fn)

def request_value(data, key, default_value = None):
    '''
    given json object and request key, if key does not exist, return None
    if default_value is specified, will return default value if value not
    found
    '''
    ret = default_value
    try:
        ret = data[key]
    except:
        print('key "{}" not found, will use default_value'.format(key))
    return ret


def main():
    file = 'nosuchfile'
    data = read_jsonfile(file)
    if data == None:
        return



if __name__ == '__main__':
    main()
