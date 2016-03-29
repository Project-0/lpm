#!/usr/bin/python

import git

def init_empty_git_repository(at_path):
    """  Create a new bare repository to serve from 

    Does not have a working directory
    """

    return git.Repo.init(at_path, bare=True, mkdir=True)


def init_working_git_repository(at_path):
    """ Creates an empty Git repository `at_path` with a working directory """

    return git.Repo.init(at_path, mkdir=True)


def clone_from(clone_url, output_path):
    """ Returns an instance of git.Repo 

    >>> cr = clone('file:///srv/git/test.git', '~/Projects/test')
    >>> cr.working_tree_directory
    "~/Projects/test"
    """
    
    return git.Repo.clone_from(clone_url, output_path)


def open_repository(at_path):
    """ Returns a Git Repo instance pointing `at_path` """
    
    return git.Repo(at_path)






















































