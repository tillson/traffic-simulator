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

    server = FTPServer(("127.0.0.1", 21), handler)
    server.serve_forever()

#
# # HTTP Server Code
# if ENABLE_HTTP:
#
#
# # Telnet Server Code
# if ENABLE_TELNET:



# Data
