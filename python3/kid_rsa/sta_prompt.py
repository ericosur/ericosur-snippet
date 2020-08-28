'''
prompt dialog of pythonista
'''


# for pythonista
#import clipboard
HAS_CONSOLE_MODULE = False
try:
    import console
    HAS_CONSOLE_MODULE = True
except ImportError:
    print('[ERROR] No console module of pythonista')


def prompt_input(msg: str):
    ''' prompt, return 0 if invalid '''
    if not HAS_CONSOLE_MODULE:
        return 0

    ret = console.input_alert(msg)
    val = 0
    try:
        val = int(ret)
        if val <= 0:
            raise ValueError
    except ValueError:
        print('{} not a number'.format(ret))
        print('invalid number, use random number:', val)
    return val

def prompt_alert(msg: str):
    ''' alert '''
    if not HAS_CONSOLE_MODULE:
        print(msg)
    else:
        console.alert(msg)

def has_console():
    ''' return true if console available '''
    return HAS_CONSOLE_MODULE

def main():
    ''' main '''
    print()
    print('Has console module of pythonista? ', end='')
    if has_console():
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
