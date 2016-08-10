#!/usr/bin/env python

""" Tests the `LPMApplication` class, instance and major operations """

import unittest
from lpm.application import LPMApplication


class TestLPMApplicationClass(unittest.TestCase):
    """ Tests the `LPMApplication`'s class interface """

    # Tests
    def test_create_instance(self):
        """ Assert `cls.__init__()` """

        app = LPMApplication()

        self.assertIsInstance(app, LPMApplication)
