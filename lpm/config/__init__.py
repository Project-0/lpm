#!/usr/bin/python

import LPMConfigParser
import os, io

DEFAULT_SETTINGS = """
[General]
project_root_path=/opt/projects.lpm/
template_path=~/.lpm/templates/
"""

DEFAULT_SEARCH_PATH =  ["{}/".format(os.getcwd()),
                        "{}/".format(os.path.expanduser("~")),
                        "/usr/local/etc/", "/usr/etc/", "/etc/"]


def find_config_files(filename='.lpm.conf', search_paths = DEFAULT_SEARCH_PATH):
    """ Looks for the config file to load when ``lpm`` loads """
    files_found = []
    for path in search_paths:
        full_file_reference = "{}{}".format(path, filename)
        if os.path.isfile(full_file_reference):
           files_found.append(full_file_reference)

    return files_found


