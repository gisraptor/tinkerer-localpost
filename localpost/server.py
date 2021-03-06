'''
    Tinkerer-Localpost server
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Handles serving the blog locally for review.

    :copyright: Copyright 2013, Nathan Hawkes
    :license: FreeBSD, see LICENCE file
'''
import sys
import os
import tinkerer
from tinkerer import paths

if sys.version_info[0] == 2:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
    from SocketServer import ThreadingMixIn
elif sys.version_info[0] == 3:
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    from socketserver import ThreadingMixIn

IP = 'localhost'

class ThreadingSimpleHTTPServer(ThreadingMixIn, HTTPServer):
    '''
    The class wraps in threading to the HTTP server to allow it to handle
    multiple requests at once.
    '''
    pass

def serve(port):
    '''
    This method serves the blog locally on the specified port.
    '''
    os.chdir(paths.root)
    handler = SimpleHTTPRequestHandler
    httpd = ThreadingSimpleHTTPServer((IP, port), handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

