#!/usr/bin/python
#
# Live Network Traffic Simulator
# Client
# Porter-Gaud Honors Computer Science IV 2017-2018
# Tillson Galloway
#
import schedule
import time
from ftplib import FTP


# Configuration
FTP_IP = "localhost"
HTTP_URL = ""
HTTPS_URL = ""
TELNET_IP = ""


# FTP Job
def ftpjob():
    print "Running FTP simulation..."
    ftp = FTP('')
    ftp.connect(FTP_IP, 21)
    time.sleep(1.5)
    ftp.login('root', 'thisisabadpassword')
    time.sleep(1.5)
    ftp.cwd('/')
    time.sleep(1.5)
    ftp.retrbinary('RETR flag.txt', open('/dev/null', 'wb').write)
    time.sleep(10)
    ftp.quit()


# Telnet Job


# HTTP Job

schedule.every(20).seconds.do(ftpjob)
while 1:
    schedule.run_pending()
    time.sleep(1)
