'''

伊呂波歌 / いろは唄

いろはにほへと
ちりぬるを
わかよたれそ
つねならむ
うゐのおくやま
けふこえて
あさきゆめみし
ゑひもせす


https://zh.wikipedia.org/wiki/%E4%BC%8A%E5%91%82%E6%B3%A2%E6%AD%8C

諸行無常　是生滅法
生滅滅已　寂滅爲樂

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

Usually we use a,i,u,e,o to sort the hiragana characters.
In old times or some special cases, the sort order is ilohani...
The script prints the index numbers for reference.

'''

from ab import hira1d

# いろは唄
ilohani = '''
いろはにほへと
ちりぬるを
わかよたれそ
つねならむ
うゐのおくやま
けふこえて
あさきゆめみし
ゑひもせす
'''


def main():
    ''' main '''
    s = ilohani.strip()
    for i in s.splitlines():
        ln = list(i.strip())
        for c in ln:
            # start from 1
            idx = hira1d.index(c) + 1
            print(f'{c}{idx:2d}', end=' ')
        print()

if __name__ == '__main__':
    main()
