#!/usr/bin/python

import unittest
import os
import re, tarfile

from quarks import map_path, rget


class LPMTestCase(unittest.TestCase):
    """ Extends the standard `unittest.TestCase` to support LPM's fixtures and special assertions 

    One of the fuctions of `LPMTestCase` is to build an extension to `unittest.TestCase` that provides
    a greater range of tests that can be performed.  The first of these is a fixtures function that
    gives the test case access to files that can be provided as expected output.

    TODO: allow `_fixture_root` to inherit its value from a parent TestSuite.  I imagine that at 
    some point, we will want to be able to group these in a fashion that is independant of the 
    file system.
    """

    _fixture_root = '/fixtures/'    # always defaults to a path relative to the file being executed
    _fixtures = {}
    _filters = []
    
    @classmethod
    def setUpClass(cls):

        def _run_filter(args, filter_set):
            """ Runs the provided args through the given filter """
            key, value = args
            rexp, func = filter_set

            if os.path.exists(value):
                if re.search(rexp, key):
                   return key, func(value)
            return key, value 
            
        mapped = map_path("{}/{}".format(os.path.split(__file__)[0], cls._fixture_root))['']
        cls._fixtures = {key: reduce(_run_filter, cls._filters, (key, value))[1] for key, value in mapped.iteritems()}

    @property
    def fixtures(self):
        """ Returns a dictionary mapping the contents of the path specified by `self._fixture_root` 

        >>> self.fixtures['readme.md'].read()
        Contents of `readme.md`
        """

        # A generator like the one below could probably provide this with very little effort
        # return {item.name : file(item.path) for item in os.walk(os.path.walk(__FILE__/self._fixture_root)}

        return self._fixtures
        
    def assertDirectoryEquals(self, target_path, expected_result, message=""):
        """ Adds an assertion to verify that a file path matches the structure of a tar file

        It should be noted that at this point, the assertion is considered true if the target path
        *exactly* matches the tarball.

        @param target_path:  a string representation of the path to analyze.  This should be provided
            in an os safe format for now and should always be an absoulte path.
        @param expected result: a tar object with the tree to compare against
        @retuns: I will have to look up how to properly extend a unittest assertion...
        @sa: `assertDirectoryContains`

        >>> self.assertDirectoryEquals('~/.lpm/', self.fixtures['git_bare.tar'])
        """

        # Assert the parameter types.  Being a unittest, I don't think duck typing is safe
        self.assertIsInstance(target_path, str)
        self.assertTrue(os.path.exists(target_path))
        self.assertIsInstance(expected_result, tarfile.TarFile)
        
        target_directory = map_path(target_path)

        # assert that walking the tarball and the target path both return a valid structure
        for item in expected_result:
            # yeilds a tarfile.TarInfo instance for each member in the archive
            try:
                rget(target_directory, item.path.split('/')[1:])
            except KeyError as e:
                raise e

    def assertDirectoryContains(self, target_path, expected_result, message):
        """ As `assertDirectoryEqual` except that the target_path needs to contain *at least* the structure of the tarball """

        pass





















