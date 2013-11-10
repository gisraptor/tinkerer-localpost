'''
    Test utilities
    ~~~~~~~~~~~~~~

    Base test case class inherited by all test cases. Utility functions.

    :copyright: Copyright 2013, Nathan Hawkes
    :license: FreeBSD, see LICENSE file
'''
import datetime
import os
import shutil
import sys
from tinkerer import cmdline, draft, output, page, paths, post, writer
from localpost import server
import types
import unittest


# test root directory
TEST_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "root"))


# stored test instance to assert from extensions while running Sphinx build
test = None


# base tinkerer test case
class BaseLocalpostTest(unittest.TestCase):
    # common setup
    def setUp(self):
        output.quiet = True
        setup()
        # add in test post
        self.test_post = post.create('My Post', datetime.date.today())
        # add in test page
        self.test_page = page.create('My Page')
        # add in test draft
        self.test_draft = draft.create('My Draft')
        # move draft to preview status
        self.test_preview = post.move(self.test_draft)
        self.build()


    # invoke build
    def build(self):
        print("")
        self.assertEquals(0, cmdline.build())


    # common teardown - cleanup working directory
    def tearDown(self):
        cleanup()


# setup blog using TEST_ROOT working directory
def setup():
    # create path
    if not os.path.exists(TEST_ROOT):
        os.mkdir(TEST_ROOT)

    paths.set_paths(TEST_ROOT)

    # setup blog
    writer.setup_blog()


# cleanup test directory
def cleanup():
    if os.path.exists(TEST_ROOT):
        shutil.rmtree(TEST_ROOT)


# used by Sphinx to lookup extensions
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
