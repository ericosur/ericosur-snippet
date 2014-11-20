# -*- coding: utf8 -*-

# http://blog.ez2learn.com/2010/03/29/python-error-mail-repor/

import logging
import logging.handlers
 
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

