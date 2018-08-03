# -*- coding: utf8 -*-

'''
reference from:
http://blog.ez2learn.com/2010/03/29/python-error-mail-repor/
'''

from __future__ import print_function

#import logging
#import logging.handlers


def main():
    '''
    main function

    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.ERROR)
    handler = logging.handlers.SMTPHandler(
        mailhost='smtp.example.com',
        fromaddr='marines@starcraft2.com',
        toaddrs='player@starcraft2.com',
        subject="Houston, We've Got a Problem",
        credentials=('username', 'password')
    )
    rootLogger.addHandler(handler)

    log = logging.getLogger(__name__)
    log.fatal('HELP! We are under attack!')
    '''

    print('just read the code, sample does not work ==>')
    print(__doc__)
    print(main.__doc__)


if __name__ == '__main__':
    main()
