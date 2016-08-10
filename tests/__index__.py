#!/usr/bin/env python

""" Establishes a collection of unit tests for the lpm package

It should be noted that at this point, from `lpm.git/`, the command
`python -m unittest discover` returns the tests in the `lpm` package, but
not the ones in the `tests` subdirectory.  The only way to run a file with
`unittest.TestCase`s is to be executing the command from the directory that
the file resides in.

TODO: I suspect that the problem is a mis-naming of the folders or files that
prevents the unittest discovery method from finding the files.
"""
