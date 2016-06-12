#!/usr/bin/env python

""" Defines an application object interface """

import io
import sys
import os
import argparse
import yaml

from lpm.config.LPMConfigParser import LPMConfigParser
from lpm.config import DEFAULT_SETTINGS, find_config_files
from lpm.functions import make_template as make_template_func
from lpm.functions import init_project as init_project_func


class LPMApplication(object):
    """ Exposes the module interface
    """

    _config_file = LPMConfigParser
    _templates = list()
    _args = None
    _template_paths = list()
    _parser = None

    def __init__(self):
        """ Create an instance of the application """

        defaults = io.BytesIO(DEFAULT_SETTINGS)
        self._config_file = LPMConfigParser()
        self._config_file.readfp(defaults)
        self._config_file.read(find_config_files())

    def index_templates(self, paths=None):
        """ Indexes the available templates """

        def _clean_path(path):
            """
            >>> path = "~/.lpm/"
            >>> _clean_path(path)
            /home/lpm_user/.lpm/templates/index.yaml
            """

            resolve_home = os.path.expanduser(path)
            add_default_file = "{}index.yaml".format(resolve_home)
            absolute_path = os.path.abspath(add_default_file)
            return absolute_path

        self._template_paths = [self._config_file.get('General',
                                                      'template_path')]
        if paths:
            for path in paths:
                self._template_paths.append(path)

        for path in self._template_paths:
            self._templates.append(yaml.load(open(_clean_path(path))))

    def build_cli_parsers(self):
        """ Assembles the `argparse` subparsers used by the application """

        def _mktempl(subparsers):
            """ Define the `mktempl` command """

            help_text = 'Create a new LPM template from source'
            inpath_help = "The fully qualified path to the directory that" \
                          " will be used as the template's source"

            make_template = subparsers.add_parser('mktempl', help=help_text)
            make_template.set_defaults(func=make_template_func)
            make_template.add_argument('-i', '--inpath',
                                       help=inpath_help,
                                       metavar="<path>", default=os.getcwd(),
                                       type=str)
            make_template.add_argument('-o', '--outpath',
                                       help="The output filename",
                                       metavar="<path/>>",
                                       default=self._template_paths[0],
                                       type=str)
            return subparsers

        def _init_project(subparsers):
            """ Define the `init_project` command """

            help_text = 'Create a new local project'
            project_folder = self._config_file.get('General',
                                                   'project_root_path')
            safe_path = os.path.expanduser(project_folder)

            init_project = subparsers.add_parser('init', help=help_text)
            init_project.set_defaults(func=init_project_func)

            init_project.add_argument('name', metavar="<project name>",
                                      type=str,
                                      help="The name of the new project")
            init_project.add_argument('-t', '--template', type=str,
                                      help='The name of the template to use')
            init_project.add_argument('-o', '--output', type=str,
                                      help='Project root directory',
                                      default=safe_path)
            return subparsers

        default_parsers = [
            _mktempl,
            _init_project
        ]

        self._parser = argparse.ArgumentParser()
        subparsers = self._parser.add_subparsers()

        subparsers = [p(subparsers) for p in default_parsers]
        return self._parser

    def run(self):
        """ Build the instruction and execute it """

        def make_args(args, config_file):
            """ Creates an LPM.Instruction() """

            kwargs = {'config_file': config_file}
            for arg in args._get_kwargs():
                if arg[0] == 'func':
                    continue
                kwargs[arg[0]] = arg[1]
            return kwargs

        self._args = self._parser.parse_args()
        self._args.func(**make_args(self._args, self._config_file))

    @classmethod
    def main(cls):
        """ Execute python module entrypoint """

        path_to_here = os.path.dirname(sys.argv[0])
        safe_path = os.path.abspath(os.path.join(path_to_here))

        app = cls()
        app.index_templates("{}/templates/".format(safe_path))
        app.build_cli_parsers()
        app.run()

        return app
