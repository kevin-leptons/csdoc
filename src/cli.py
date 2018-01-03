#!/usr/bin/env python3

'''
SYNOPSIS

    csdoc list [docname]
    csdoc open docname
    csdoc map
    csdoc -v, --version
    csdoc -h, --help

DESCRIPTIONS

    *list* show all document relate with keyword

    *info* show information about course

    *open* open docname in format <course>.<unit>


EXAMPLES

    $ csdoc open cs103.001

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''

import os
import sys
import sqlite3
from os import path
from os.path import dirname, realpath, isfile, basename
from subprocess import Popen, CalledProcessError, DEVNULL

VERSION = "maj.min.rev"
DEB_VERSION = "0"
ROOT = dirname(dirname(realpath(__file__)))
DB_PATH = path.join(ROOT, 'dest/csdoc.db')
COURSE_PATH = path.join(ROOT, 'src/course')


def call(args, cwd=None):
    exit_code = Popen(args, cwd=cwd).wait()
    if exit_code != 0:
        raise CalledProcessError(exit_code, args)

def cli_help():
    exe_name = basename(sys.argv[0])

    print('USAGE')
    print('    map                  Show map to learn')
    print('    list [course]        List courses or units of course')
    print('    open course.unit     Open document')
    print('    -v, --version        Print version')
    print('    -h, --help           Print help')
    
    print()
    print('EXAMPLES')
    print('     %s list' % (exe_name))
    print('     %s list cs103' % (exe_name))
    print('     %s open cs103.001' % exe_name)


def unit_path(cid, uid):
    return path.join(COURSE_PATH, cid, '%s.pdf' % (uid))


def limit_str(str, lim):
    if len(str) >= lim:
        return str[:lim - 3] + '...'
    else:
        return str


def cli_map():
    print('OS       cs140 => cs240')
    print('Core     cs106b => cs107 => cs110')
    print('         cs103 => cs109 => cs161')
    print('AI       math19 => math20 => math21 => phys41 => phys43 => cs221')

    print()
    print('http://csmajor.stanford.edu/Requirements.shtml')


def cli_list(id=None):
    if id is None:
        cli_list_course()
    else:
        cli_list_unit(id)


def cli_list_course():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    rows = cur.execute('SELECT * FROM course ORDER BY id')
    for row in rows:
        print('%-9s %-69s' % (row[0], limit_str(row[1], 69)))

    con.close()


def cli_list_unit(cid):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    # course info
    cur.execute('SELECT * FROM course WHERE id="%s"' % (cid))
    course = cur.fetchone()
    if course is None:
        print('Not found course')
        sys.exit(1)
    print(limit_str(course[1], 79).upper())
    print(course[2])

    # list units of course 
    cur.execute('SELECT * FROM unit WHERE cid="%s"' % (cid))
    for row in cur:
        print('%-3s   %s' % (row[1], limit_str(row[2], 72)))

    con.close()


def cli_open(docname):
    names = docname.split('.')
    if len(names) != 2:
        cli_help()
        sys.exit(1)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    query = 'SELECT * FROM unit WHERE cid="{}" AND uid="{}"'.format(
        names[0], names[1]
    )
    cur.execute(query)
    row = cur.fetchone()
    if row is None:
        print('Not found unit')
        sys.exit(1)

    pdf_doc = unit_path(names[0], names[1])
    if not isfile(pdf_doc):
        print('Missing unit document: %s' % (pdf_doc))
        sys.exit(1)
    Popen(['xdg-open', pdf_doc], stdout=DEVNULL, stderr=DEVNULL) 
    con.close()


def cli():
    # not match with any commands
    if len(sys.argv) < 2:
        cli_help()
        sys.exit(1)
    if sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print(VERSION)
        return
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        cli_help()
        return

    # commands
    if sys.argv[1] == 'map':
        cli_map()
    elif sys.argv[1] == 'list':
        if len(sys.argv) == 2:
            cli_list()
        else:
            cli_list(sys.argv[2])
    elif sys.argv[1] == 'open':
        if len(sys.argv) != 3:
            cli_help()
            sys.exit(1)
        cli_open(sys.argv[2])
    else:
        cli_help()
        sys.exit(1)

cli()
