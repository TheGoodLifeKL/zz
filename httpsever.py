# coding:utf-8

import http.server
import SocketServer

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",PORT),Handler)
print("server at port",PORT)
httpd.server_forever()