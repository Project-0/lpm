#!/usr/bin/python

""" Define UnitTest TestSuite to cover the Git integration """

import lpm_unittest
import func_git

class TestGitModule(lpm_unittest.LPMTestCase):
    """ Asserts the high-level functions of the Git Module """

    
    def setUp(self):
        pass

    
    def tearDown(self):
        # clean up test paths
        # os.remove('/tmp/test_init_bare.git', recursive=True)
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
        # With
        output_path = '/tmp/test_init_bare.git'
        
        # Given
        target_new_repo = func_git.init_empty_git_repository(output_path)

        # Assert
        print self.fixtures
        self.assertDirectoryEquals(target_new_repo, self.fixtures['git_init_bare.tar'])


    def test_clone(self):
        """ Clone a target repository to a specified directory """

        pass
    
