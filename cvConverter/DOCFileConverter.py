from cvConverter.BaseConverter import BaseConverter
from subprocess import Popen, PIPE

__author__ = 'siwei'

class DOCFileConverter(BaseConverter):

    def __init__(self):
        self.type = "doc"

    def convert(self):
        cmd = ['antiword', self.path]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')