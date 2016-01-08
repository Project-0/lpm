#!/usr/bin/python

import git

def init_empty_git_repository(at_path):
    """  Create a new bare repository to serve from 

    Does not have a working directory
    """
    
    raise NotImplementedError("Git operations are non-functional")

def clone(clone_url, output_path):
    """ Returns an instance of git.Repo 

    >>> cr = clone('file:///srv/git/test.git', '~/Projects/test')
    >>> cr.working_tree_directory
    "~/Projects/test"
    """
    
    raise NotImplementedError("Git operations are non-functional")
