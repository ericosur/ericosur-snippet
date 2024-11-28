#!/usr/bin/env python3
# coding: utf-8

''' test translate_weekday '''

from new_date import translate_weekday


def test_result(wd, expected):
    ''' test_result '''
    try:
        r = translate_weekday(wd)
        assert r == expected
        print(f'input: {wd}, expect: {expected}')
    except ValueError as e:
        print(e, wd)


def main():
    ''' main '''
    test_result(0, 1)
    test_result(1, 2)
    test_result(2, 3)
    test_result(3, 4)
    test_result(4, 5)
    test_result(5, 6)
    test_result(6, 0)
    test_result(-1, None)
    test_result(7, None)


if __name__ == '__main__':
    main()
