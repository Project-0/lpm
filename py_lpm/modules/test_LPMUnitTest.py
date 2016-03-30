#!/usr/bin/python

import unittest
import os

class LPMTestCase(unittest.TestCase):
    """ Extends the standard `unittest.TestCase` to support LPM's fixtures and special assertions 

    One of the fuctions of `LPMTestCase` is to build an extension to `unittest.TestCase` that provides
    a greater range of tests that can be performed.  The first of these is a fixtures function that
    gives the test case access to files that can be provided as expected output.

    TODO: allow `_fixture_root` to inherit its value from a parent TestSuite.  I imagine that at 
    some point, we will want to be able to group these in a fashion that is independant of the 
    file system.
    """

    _fixture_root = os.path.join(__file__, '/fixtures/')    # always defaults to a path relative to the file being executed

    @property
    def fixtures(self):
        """ Returns a dictionary mapping the contents of the path specified by `self._fixture_root` 

        >>> self.fixtures['readme.md'].read()
        Contents of `readme.md`
        """

        # A generator like the one below could probably provide this with very little effort
        # return {item.name : file(item.path) for item in os.walk(os.path.walk(__FILE__/self._fixture_root)}

        return {item for item in os.walk(self._fixture_root)}
       
    def assertDirectoryEquals(self, target_path, expected_result, message):
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
        # assert that walking the tarball and the target path both return a valid structure

        pass

    def assertDirectoryContains(self, target_path, expected_result, message):
        """ As `assertDirectoryEqual` except that the target_path needs to contain *at least* the structure of the tarball """

        pass
