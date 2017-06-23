'''
SYNOPSIS

    pack_debian(spec)

DESCRIPTION

    Pack this project ot Debian package.

AUTHORS

    Kevin Leptons <kevin.leptons@gmai.com>
'''

import os
import shutil
from os import path
from stat import S_IXUSR, S_IXGRP, S_IXOTH, S_IRUSR, S_IRGRP, S_IROTH

from .error import MissingStepError
from .shell import cp, chmod, call, rm, mkdir


root = os.path.realpath(path.join(os.path.dirname(__file__), '..'))
_CLI_FILE = path.join(root, 'src', 'cli.py')
_BUILD_STEP_SOURCE = 'build-source'
_FMOD_EXE = S_IXUSR | S_IXGRP | S_IXOTH | S_IRUSR | S_IRGRP | S_IROTH


def pack_debian(spec):
    if not path.isdir(spec.dest):
        raise MissingStepError(_BUILD_STEP_SOURCE)

    # file system
    dist_fs = path.join(spec.dist, spec.deb_name)
    dist_bin = path.join(dist_fs, 'bin')
    src_deb_dir = path.join(spec.src, 'pkg/DEBIAN')
    dist_deb_dir = path.join(dist_fs, 'DEBIAN')
    dist_man_1 = path.join(dist_fs, 'usr/share/man/man1')
    src_csdoc = path.join(spec.src, 'course')
    dist_csdoc = path.join(dist_fs, 'usr/share/doc/csdoc')
    src_dbfile = path.join(spec.dest, 'csdoc.db')
    dist_dbfile = path.join(dist_csdoc, 'csdoc.db')
    rm(spec.dist)
    mkdir(dist_bin)
    mkdir(dist_man_1)

    # debian directory
    cp(src_deb_dir, dist_deb_dir)
    src_deb_control = path.join(src_deb_dir, 'control')
    dist_deb_control = path.join(dist_deb_dir, 'control')
    f = open(src_deb_control, 'r')
    data = f.read()
    f.close()
    data = data.replace('{version}', spec.version.deb_ver)
    f = open(dist_deb_control, 'w')
    f.write(data)
    f.close()
    dist_deb_preinst = path.join(dist_deb_dir, 'preinst')
    dist_deb_postinst = path.join(dist_deb_dir, 'postinst')
    dist_deb_prerm = path.join(dist_deb_dir, 'prerm')
    dist_deb_postrm = path.join(dist_deb_dir, 'postinst')
    chmod(dist_deb_preinst, _FMOD_EXE)
    chmod(dist_deb_postinst, _FMOD_EXE)
    chmod(dist_deb_prerm, _FMOD_EXE)
    chmod(dist_deb_postrm, _FMOD_EXE)

    # create man page
    dest_man = path.join(spec.dest, 'man/csdoc.1.gz')
    dist_man = path.join(dist_man_1, 'csdoc.1.gz')
    cp(dest_man, dist_man)

    # command line
    f = open(path.join(spec.src, 'cli.py'), 'r')
    cli_data = f.read()
    f.close()
    cli_data = cli_data.replace('maj.min.rev', spec.version.pkg_ver)
    dist_cli = path.join(dist_bin, spec.name)
    f = open(dist_cli, 'w')
    f.write(cli_data)
    f.close()
    chmod(dist_cli, _FMOD_EXE)

    # copy document files 
    cp(src_csdoc, dist_csdoc)
    
    # copy database
    cp(src_dbfile, dist_dbfile)

    # build debian package
    call(['dpkg-deb', '--build', '-D', dist_fs, spec.dist])
