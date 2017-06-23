'''
SYNOPSIS

    build_csdoc(pkg_spec)

DESCRIPTION

    Scan src/course to get metadata of courses, then put data into sqlite
    database.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''

import sqlite3
import yaml
from os import path, listdir
from os.path import isdir, isfile

from .error import MissingUnitError
from .shell import mkdir, rm


def _scan_course(dpath):
    index_file = path.join(dpath, 'index.yaml')
    f = open(index_file, 'r')
    index_raw = f.read()
    f.close()
    index = yaml.load(index_raw)


    # verify units
    for i in range(len(index['units'])):
        fpath = path.join(dpath, "%03d.pdf" % (i + 1))
        if not isfile(fpath):
            raise MissingUnitError(fpath, index['units'][i])

    return index


def build_csdoc(pkg_spec):
    src_dir = path.join(pkg_spec.src, 'course')
    dbfile = path.join(pkg_spec.dest, 'csdoc.db')
    mkdir(pkg_spec.dest)
    rm(dbfile)

    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    cur.execute('CREATE TABLE course (id text, name text, url text)')
    cur.execute('CREATE TABLE unit (cid text, uid text, name text)')
    con.commit() 

    doc_dirs = [f for f in listdir(src_dir) if isdir(path.join(src_dir, f))]
    for d in doc_dirs:
        # course info
        c = con.cursor()
        info = _scan_course(path.join(src_dir, d))
        query = 'INSERT INTO course VALUES ("{}", "{}", "{}")'.format(
            info['id'], info['name'], info['url']
        )
        c.execute(query)

        # units of course
        for i in range(len(info['units'])):
            uid = "%03d" % (i + 1)
            query = 'INSERT INTO unit VALUES ("{}", "{}", "{}")'.format(
                info['id'], uid, info['units'][i]
            )
            c.execute(query)

        con.commit()

    con.close()
