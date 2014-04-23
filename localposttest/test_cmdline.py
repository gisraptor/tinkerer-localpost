'''
    Command Line Test
    ~~~~~~~~~~~~~~~~~

    Tests Tinkerer-Localpost command line.

    :copyright: Copyright 2013, Nathan Hawkes
    :license: FreeBSD, see LICENSE file
'''
import os
import sys
import datetime
import tinkerer
from localposttest import utils
from localpost import cmdline

# mock server to allow testing cmdline without spinning up the server
class MockServer(object):
    # Mock serve method
    def serve(self, port):
        print('Mocking server on port %i' % port)

# test localpost command line
class TestCmdLine(utils.BaseLocalpostTest):
    # setup mock server
    def setUp(self):
        utils.paths.set_paths(utils.TEST_ROOT)
        utils.BaseLocalpostTest.setUp(self)
        utils.BaseLocalpostTest.build(self)
        self.orig_server = cmdline.server
        cmdline.server = MockServer()


    # re-enable original server
    def tearDown(self):
        cmdline.server = self.orig_server
        utils.BaseLocalpostTest.tearDown(self)


    # test blog serve
    def test_serve(self):
        cmdline.main(["--serve", "8000"])

        dirlist = os.listdir(utils.paths.root)
        dirlist.sort()
        expected = [
            "_static",
            "_templates",
            "blog",
            "drafts",
            "conf.py",
            "index.html",
            tinkerer.master_doc + ".rst"
        ]
        expected.sort()
        self.assertEqual(dirlist, expected)


    # ensure localpost runs from any of the folders under
    # the blog root
    def test_run_anywhere(self):
        # move outside the blog root
        curdir = os.getcwd()
        os.chdir(utils.paths.blog)

        # serving the blog should work from anywhere
        self.assertEqual(0,
                cmdline.main(["--serve", "8000"]))

        # return to the original directory to allow for proper cleanup
        os.chdir(curdir)
