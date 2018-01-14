import json

def read_setting(filename):
    #home = os.environ.get('HOME')
    # read from json file
    with open(filename) as sec_file:
        data = json.load(sec_file)
    return data
