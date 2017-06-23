'''
SYNOPSIS

    call(args, cwd=None)
    cp(src, dest)
    rm(path)
    chmod(path, mod)

DESCRIPTION

    Bash interface functions.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''

import os
from subprocess import Popen, CalledProcessError
from os import makedirs, remove
from os.path import isdir, isfile, exists, basename
from shutil import copyfile, copytree, rmtree


def call(args, cwd=None):
    exit_code = Popen(args, cwd=cwd).wait()
    if exit_code != 0:
        raise CalledProcessError(exit_code, args)


def _cp_dir(src, dest, exist_ignore):
    if isdir(dest):
        dest_dir = os.path.join(dest, basename(src))
        if isdir(dest_dir) and exist_ignore:
            return dest_dir
        copytree(src, dest_dir)
        return dest_dir
    else:
        copytree(src, dest)
        return dest


def _cp_file(src, dest, exist_ignore):
    if isfile(dest) and exist_ignore:
        return dest
    if isdir(dest):
        dest_file = os.path.join(dest, basename(src))
        copyfile(src, dest_file)
        return dest_file
    else:
        copyfile(src, dest)
        return dest


def cp(src, dest, exist_ignore=True):
    if isdir(src):
        return _cp_dir(src, dest, exist_ignore)
    else:
        return _cp_file(src, dest, exist_ignore)


def rm(path, exist_ignore=True):
    if (not exists(path)) and exist_ignore:
        return
    if isdir(path):
        rmtree(path)
    else:
        remove(path)


def mkdir(path):
    if not isdir(path):
        makedirs(path)


def chmod(path, mode):
    os.chmod(path, mode)
