'''
    Blog Server Test
    ~~~~~~~~~~~~~~~~

    Tests serving the static blog posts.

    :copyright: Copyright 2013, Nathan Hawkes
    :license: FreeBSD, see LICENSE file
'''
import os
import sys
import datetime
import time
from multiprocessing import Process
import tinkerer
from localposttest import utils

try:
    import urllib2 as request
except ImportError as e:
    import urllib.request as request

# create a place to send stdout when nothing should display
class NullDevice(object):
    # setup null write
    def write(self, s):
        pass

    # setup null flush
    def flush(self):
        pass


# test serving the blog
class TestServe(utils.BaseLocalpostTest):
    # setup the blog to serve
    def setUp(self):
        super(TestServe, self).setUp()

        # silence the SimpleHTTPServer
        self.orig_stderr = sys.stderr
        sys.stderr = NullDevice()

        # spin up the server for testing
        self.p = Process(target=utils.server.serve, args=(8000, ))
        self.p.daemon = True
        self.p.start()

        # setup URLs
        self.baseUrl = 'http://localhost:8000/'
        self.htmlUrl = self.baseUrl + utils.paths.html.replace(utils.paths.root,'') + '/'

    def tearDown(self):
        # clean up server
        self.p.terminate()

        super(TestServe, self).tearDown()

        # restore voice
        sys.stderr = self.orig_stderr


    # test serve call
    def test_serve(self):
        response = False

        if self.p.is_alive():
            time.sleep(5)
            page = request.urlopen(self.baseUrl)
            response = page.read()

        # assert response received
        self.assertTrue(response)


    # test serve post call
    def test_serve_post(self):
        response = False

        if self.p.is_alive():
            time.sleep(5)
            path = self.htmlUrl + self.test_post.docname + '.html'
            post = request.urlopen(path)
            response = post.read()

        # assert response received
        self.assertTrue(response)


    # test serve page call
    def test_serve_page(self):
        response = False

        if self.p.is_alive():
            time.sleep(5)
            path = self.htmlUrl + self.test_page.docname + '.html'
            page = request.urlopen(path)
            response = page.read()

        # assert response received
        self.assertTrue(response)


    # test serve draft call
    def test_serve_draft(self):
        response = False

        if self.p.is_alive():
            time.sleep(5)
            path = self.htmlUrl + self.test_preview.docname + '.html'
            draft = request.urlopen(path)
            response = draft.read()

        # assert response received
        self.assertTrue(response)


