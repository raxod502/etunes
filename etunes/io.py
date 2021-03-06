import os
import shutil
import subprocess
import sys
import tempfile
import traceback

class StandardIO:
    def __init__(self):
        self.DEVNULL = subprocess.DEVNULL
        self.PIPE = subprocess.PIPE
        self.abspath = os.path.abspath
        self.chdir = os.chdir
        self.dirname = os.path.dirname
        self.environ = os.environ
        self.exists = os.path.exists
        self.get_terminal_size = shutil.get_terminal_size
        self.getcwd = os.getcwd
        self.isdir = os.path.isdir
        self.isfile = os.path.isfile
        self.islink = os.path.islink
        self.join = os.path.join
        self.link = os.link
        self.makedirs = os.makedirs
        self.mkdir = os.mkdir
        self.NamedTemporaryFile = tempfile.NamedTemporaryFile
        self.open = open
        self.print = print
        self.print_exc = traceback.print_exc
        self.realpath = os.path.realpath
        self.rename = os.rename
        self.replace = os.replace
        self.run = subprocess.run
        self.splitext = os.path.splitext
        self.stderr = sys.stderr
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.which = shutil.which
