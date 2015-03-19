#!/usr/bin/env python

'''
code snippet from:
http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python

getpass:
stackoverflow.com/questions/1761744/python-read-password-from-stdin
'''

def send_email():
    import smtplib
    import getpass

    fromaddr = 'scl064810@gmail.com'
    toaddr = 'ericosur@gmail.com'
    username = 'scl064810@gmail.com'
    password = getpass.getpass('password for ' + username + ' : ')
    msg = "\r\n".join([
        "From: scl064810@gmail.com",
        "To: ericosur@gmail.com",
        "Subject: Just test message",
        "",
        "why, oh, why"
        ])

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddr, msg)
        server.close()
    except:
        print "failed to send gmail"

if __name__ == '__main__':
    send_email()
