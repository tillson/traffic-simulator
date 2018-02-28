#!/usr/bin/python
#
# Live Network Traffic Simulator
# Server
# Porter-Gaud Honors Computer Science IV 2017-2018
# Tillson Galloway
#
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

import SimpleHTTPServer
import SocketServer

import socket
import sys
from thread import *



# Configuration
ENABLE_FTP = True
ENABLE_HTTP = True
ENABLE_TELNET = True

FTP_PASSWORD = "thisisabadpassword"
TELNET_PASSWORD = "abc123!!!"

# FTP Server Code
if ENABLE_FTP:
    authorizer = DummyAuthorizer()
    root = os.path.dirname(os.path.realpath(__file__)) + "/ftp_server"
    print root
    authorizer.add_user("root", FTP_PASSWORD, root, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(('', 21), handler)
    server.serve_forever()


# HTTP Server Code
if ENABLE_HTTP:
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(('', 80), Handler)
    httpd.serve_forever()


# Telnet Server Code
if ENABLE_TELNET:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('', 5555))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    s.listen(10)
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,))

    s.close()

def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n')
    while True:
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()
