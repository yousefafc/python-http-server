#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import os

PORT = 9000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/public")
httpd.serve_forever()

