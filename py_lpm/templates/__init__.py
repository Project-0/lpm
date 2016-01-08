
import os

class LPMTemplate(object):

    def __init__(self, inpath=None, tar_path=None):
        self._inpath = inpath
        self._tar_path = tar_path
        self._template_name = os.path.basename(inpath) 

    @property
    def inpath(self):
        return self._inpath

    @inpath.setter
    def inpath(self, value):
        if os.path.isdir(value):
            self._inpath = value
        else:
            raise ValueError("{} is not a valid directory.  --inpath must be the full path to the source directory".format(inpath))

    @property
    def tar_path(self):
        return self._tar_path

    @tar_path.setter
    def tar_path(self, value):
        if os.path.isdir(value):
            self._tar_path = value
        else:
            raise ValueError("{} is not a valid directory.  --outpath must be the full path to the distination directory".format(inpath))

    @property
    def tarfile(self):
        return "{}/{}.tar".format(self._tar_path, self._template_name)
    





