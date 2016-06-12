#!/usr/bin/python

""" Defines the functional pattern for working with the py_lpm module
"""

import os
import tarfile
import virtualenv
import subprocess
import git

from templates import LPMTemplate


def get_parser(function_name):
    if isinstance(function_name, list):
        return [get_parser(f for f in function_name)]




def make_template(inpath, outpath, config_file):

    error_template = "{} is not a valid directory.  {} must be the full path to the source directory" # pylint: disable=E501
    if not os.path.isdir(inpath):
        raise ValueError(error_template.format(inpath, '--inpath'))
    if not os.path.isdir(outpath):
        raise ValueError(error_template.format(outpath, '--outpath'))

    new_template = LPMTemplate(inpath, outpath)

    print "Walking {}".format(new_template._template_name)
    with tarfile.open(new_template.tarfile, 'w:bz2') as template_tar:
        for root, directories, files in os.walk(new_template.inpath):
            for _dir in directories:
                template_tar.add(os.path.join(root, _dir), arcname=_dir)
            for _file in files:
                # TODO: This check needs to be made modular
                if _file == "virtualenv_extra_text.py":
                    extra_text = ""
                    with open(os.path.join(root, _file), "r") as etf:
                        extra_text = etf.read()
                    template_bootstrap = "{}_bootstrap.py".format(new_template._template_name)
                    with open("/tmp/{}".format(template_bootstrap), "w+") as temp_file:
                        bootstrap_buffer = virtualenv.create_bootstrap_script(extra_text)
                        temp_file.write(bootstrap_buffer)
                    template_tar.add(os.path.join("/tmp",template_bootstrap), arcname=template_bootstrap)
                else:
                    template_tar.add(os.path.join(root, _file), arcname=_file)


def init_project(name, template, output, config_file):
    """ Collects the different sources of input and sends the Instruction to lpm


    """

    archive_file = "{}.tar".format(
            os.path.join(config_file.get('General', 'template_path'), template))
    project_directory = os.path.expanduser(os.path.join(output, name))
    if not os.path.isdir(project_directory):
        try:
            os.mkdir(project_directory)
        except Exception as e:
            raise IOError("Could not create {}: {}".format(
                project_directory, e.message))

    # extract template config
    # merge with passed config into a single Instruction()
    # send instruction to submodules

    """ i.e.

    Instruction.commands = ['extract tarball',
                            'initialize git repository']

    py_lpm.execute(Instruction)
    """

    if False:  # config_file.getboolean('git', 'init_bare'):

        # This is the path that will be /srv/git/name.git/
        repo_dir = os.path.join('/srv/git', "{}.git".format(name))

        # clone_url = "file://".format(repo_dir)

        project_repo = git.Repo.init(repo_dir, bare=True)

        cloned_repo = git.Repo.clone_from(repo_dir, project_directory)
        origin = cloned_repo.remotes.origin

    with tarfile.open(archive_file, 'r:bz2') as template_tar:
        template_tar.extractall(project_directory)


    if False: # config_file.getboolean('git', 'init_bare'):
        ignore_directories = ['.git']
        for root, directories, files in os.walk(project_directory, topdown=True):

            directories[:] = [d for d in directories if d not in ignore_directories]
            relative = os.path.relpath(root, project_directory)

            to_add = [os.path.join(relative, file) for file in files]
            print to_add
            cloned_repo.index.add(to_add)

        COMMIT_MSG = "Initial commit"
        cloned_repo.index.commit(COMMIT_MSG)
        origin.push()



    bootstrap_filename = "{}_bootstrap.py".format(template)
    bootstrap_path = os.path.join(project_directory, bootstrap_filename)
    if os.path.exists(bootstrap_path):
        subprocess.call(['python', bootstrap_path, project_directory])



