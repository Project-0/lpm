#!/usr/bin/python

""" Describes the lpm application when the package is executed as a module

Use with:
``localhost$ python -m lpm`` or, if the path to this file is in the
$PATH variable, ``python lpm``
"""

import os
import sys
import io
import yaml
import argparse
import logging

from lpm.config import find_config_files, DEFAULT_SETTINGS
from lpm.config.LPMConfigParser import LPMConfigParser
from lpm.functions import make_template as make_template_func
from lpm.functions import init_project as init_project_func
from lpm.functions import settings_cmd as settings_func


def make_args(args, config_file):
    """ Creates an LPM.Instruction() """

    kwargs = {'config_file': config_file}
    for arg in args._get_kwargs():
        if arg[0] == 'func':
            continue
        kwargs[arg[0]] = arg[1]
    return kwargs


def echo(**kwargs):
    print kwargs


def main():
    """ The master function called when this package is called as a module
    """

    config_file = LPMConfigParser()
    config_file.readfp(io.BytesIO(DEFAULT_SETTINGS))
    config_file.read(find_config_files())

    if config_file.has_option('General', 'template_path'):
        template_path = config_file.get('General', 'template_path')
    else:
        template_path = "{}/templates/".format(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]))))

    full_path = "{}index.yaml".format(template_path)

    try:
        templates = yaml.load(open(os.path.expanduser(full_path), 'r+'))
    except IOError as e:
        print "No template index found in {}.  Templates will be unavailable.".format(full_path)

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Where does this show up?")

    # define 'mktempl'
    make_template = subparsers.add_parser('mktempl', help='Create a new LPM template from source')
    make_template.set_defaults(func=make_template_func)
    make_template.add_argument('-i', '--inpath',
                               help="The fully qualified path to the directory that will be used as the template's source",
                               metavar="<path>", default=os.getcwd(),
                               type=str)
    make_template.add_argument('-o', '--outpath',
                               help="The output filename", metavar="<path/>>",
                               default=template_path,
                               type=str)

    # define the 'init' command
    init_project = subparsers.add_parser('init', help='Create a new local project')
    init_project.set_defaults(func=init_project_func)
    # what I really want here is a partial function with a URI target and kwargs TBD

    init_project.add_argument('name', metavar="<project name>", type=str,
                              help="The name of the new project")
    init_project.add_argument('-t', '--template', type=str, help='The name of the template to use')
    init_project.add_argument('-o', '--output', type=str, help='Project root directory',
                              default=os.path.expanduser(config_file.get('General', 'project_root_path')))

    settings_cmd = subparsers.add_parser('settings', help='list or edit application settings')
    settings_cmd.set_defaults(func=settings_func)

    settings_cmd.add_argument('-e', '--export', type=bool, default=False, help='exports the settings')

    args = parser.parse_args()
    args.func(**make_args(args, config_file))

if __name__ == "__main__":
    main()
