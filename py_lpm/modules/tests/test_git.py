#!/usr/bin/python

""" Define UnitTest TestSuite to cover the Git integration """

import unittest

class TestGitModule(unittest.TestCase):
    """ Asserts the high-level functions of the Git Module """

    
    def setUp(self):
        pass

    
    def tearDown(self):
        pass


    @classmethod
    def setUpCls(cls):
        pass


    @classmethod
    def tearDownCls(cls):
        pass

    # Private UnitTest utility methods

    
    def _purge_filesystem(self):
        """ Removes any files created by the Test Case """

        pass


    # Test Cases

    def test_init_bare(self):
        """ Create an empty Git repository without a working directory """

        pass


    def test_clone(self):
        """ Clone a target repository to a specified directory """

        pass
    
