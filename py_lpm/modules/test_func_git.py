#!/usr/bin/python

""" Define UnitTest TestSuite to cover the Git integration """

import re, tarfile

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
    def setUpClass(cls):
        tar_filter = ('.+\.tar$', lambda path: tarfile.open(path))
        cls._filters.append(tar_filter)
        
        super(TestGitModule, cls).setUpClass()


    @classmethod
    def tearDownClass(cls):
        super(TestGitModule, cls).tearDownClass()

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
        self.assertEqual(target_new_repo.git_dir, output_path)
        self.assertDirectoryEquals(target_new_repo.git_dir, self.fixtures['git_bare.tar'])


    def test_clone(self):
        """ Clone a target repository to a specified directory """

        raise NotImplementedError("func_git.clone tests have not been written")
    
