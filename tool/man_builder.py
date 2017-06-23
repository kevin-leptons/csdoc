'''
SYNOPSIS

    build_manpage(pkg_spec)

DESCRIPTION

    Build man pages.

AUTHORS

    kevin leptons <kevin.leptons@gmail.com>
'''

import gzip

from os import path, listdir
from os.path import isfile
from datetime import datetime

from .shell import mkdir


def build_manpage(pkg_spec):
    build_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    src_dir = path.join(pkg_spec.src, 'man')
    dest_dir = path.join(pkg_spec.dest, 'man')

    mkdir(dest_dir)
    man_files = [f for f in listdir(src_dir) if isfile(path.join(src_dir, f))]
    for file_name in man_files:
        # read source file and replace correct build date and version
        # then write man page in destination
        src_file = path.join(src_dir, file_name)
        dest_file = path.join(dest_dir, path.splitext(file_name)[0]) + '.gz'
        f = open(src_file, 'r')
        data = f.read()
        f.close()
        data = data.replace('{{build_date}}', build_date)
        data = data.replace('{{version}}', pkg_spec.version.pkg_ver)
        f = gzip.open(dest_file, 'w')
        f.write(bytes(data, 'utf-8'))
        f.close()
