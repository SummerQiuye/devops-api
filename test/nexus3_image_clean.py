import subprocess
import sys
import time
import os
from config import *


class NexusImageClean:

    def __init__(self, appname):
        self.cmd = "nexus-cli image tags --name jiashu/"
        self.app = appname

    def getImageByAppname(self):
        imageResult = subprocess.Popen(self.cmd + self.app,
                                       shell=True, stdout=subprocess.PIPE)
        print(imageResult.stdout.read())

    def cleanImageByTag(self):
        pass
