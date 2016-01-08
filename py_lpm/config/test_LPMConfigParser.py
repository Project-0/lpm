#!/usr/bin/python

import unittest
import config
import os
import __builtin__

from StringIO import StringIO
from mock import patch, mock_open
from config.LPMConfigParser import LPMConfigParser

class testLPMConfigParser(unittest.TestCase):
    
    def test_ConstructConfig(self):
        """ False positive; this doesn't assert that ``find_config_file`` loads from
        the correct location, only that mocking ``open`` returns the data we gave it"""

        config_obj = LPMConfigParser()
        config_obj.readfp(config.find_config_file())
        self.assertEquals(config_obj.sections(), ['General'])
        self.assertTrue(os.path.isdir(os.path.expanduser(config_obj.get('General', 'project_root_path'))))
