#!/usr/bin/env python

import shutil
import sys
import subprocess
import os.path
import time
import string

def copy():
    path = sys.argv[1]
    name = string.split(path, '/')
    i = 0
    
    while len(name) < i:
        i = i + 1
    file = name[i-1]
    
    if (os.path.exists('/home/ubuntu/workspace/backup/' + file)):
        if (os.path.isfile('/home/ubuntu/workspace/backup/' + file)):
            os.remove('/home/ubuntu/workspace/backup/' + file)
            shutil.copyfile(path, '/home/ubuntu/workspace/backup/' + file)
        elif (os.path.isdir('/home/ubuntu/workspace/backup/' + file)):
            shutil.rmtree('/home/ubuntu/workspace/backup/' + file)
            shutil.copytree(path, '/home/ubuntu/workspace/backup/' + file)
    else:
        if (os.path.isfile(path)):
            shutil.copyfile(path, '/home/ubuntu/workspace/backup/' + file)
        elif (os.path.isdir(path)):
            shutil.copytree(path, '/home/ubuntu/workspace/backup/' + file)

copy()