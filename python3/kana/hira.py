'''
import python list from ab.py and print out

あ い う え お
か き く け こ
さ し す せ そ
た ち つ て と
な に ぬ ね の
は ひ ふ へ ほ
ま み む め も
や ？ ゆ ？ よ
ら り る れ ろ
わ ゐ ？ ゑ を
ん

'''

from ab import hiragana, katakana


def println(alist):
    ''' println '''
    msg = ''
    for c in alist:
        msg += f'{c:2s}'
    print(msg)

def main():
    ''' main '''
    for i in hiragana:
        println(i)
    for i in katakana:
        println(i)
    print()


if __name__ == '__main__':
    main()
