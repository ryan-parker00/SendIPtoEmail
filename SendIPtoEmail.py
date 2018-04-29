#!/usr/bin/python3
# Developed by Ryan Parker for Jeff Bernier 04/25/2018
#
# Provides the ability to detect the IP address of the system and send via email
# This script is specifically to be run on a Raspberry Pi
#
# References:
# Sending email: https://gist.github.com/yzhong52/d703ec82aeee24164f0c
# Reading IP Address: https://pypi.org/project/netifaces/

# Includes
import netifaces
import smtplib
from time import sleep
from myconfig import MyConfig

def getIP():
    info = netifaces.ifaddresses('eth0')
    addrs = info[netifaces.AF_INET]
    addr = addrs[0]
    return addr['addr']

def sendEmail(conf, addr):
    server = smtplib.SMTP(conf['SMTP_SERVER'], conf['SMTP_PORT'])
    server.ehlo()
    server.starttls()
    server.login(conf['USERNAME'], conf['PASSD'])

    BODY = '\r\n'.join(['To: %s' % conf['TO'],
                       'From: %s' % conf['FROM'],
                       'Subject: %s' % conf['SUBJECT'],
                       '',
                       'The address of your Raspberry Pi on eth0 is %s' % addr])

    print(BODY)
    try:
        server.sendmail(conf['USERNAME'], conf['TO'], BODY)
        print('Email Sent')
    except:
        print('Error sending email')

    server.quit()

if __name__ == "__main__":
    sleep(10)
    conf = MyConfig()
    addr = getIP()
    print(addr)
    sendEmail(conf, addr)
