#!/usr/bin/env python3

'''
SYNOPSIS

    ctl build
    ctl dist [--clear]
    ctl -h, --help

DESCRIPTION

    *build* build documents

    *build --clear* clear all of build files.

    *dist* pack theme into package in 'dist/csdoc<version>_all.deb'.

    *dist --clear* clear all of distribution files.

    *-h, --help* show help information.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''

import click
from os import path
from os.path import realpath, dirname

from tool.types import Version, PkgSpec
from tool.builder import pkg_build_clear, pkg_build, \
                         pkg_dist, pkg_dist_clear, \
                         pkg_test

ROOT = realpath(dirname(__file__))

pkg_ver = Version(0, 1, 0)
pkg_spec = PkgSpec('csdoc', pkg_ver, ROOT, path.join(ROOT, 'src'),
                   path.join(ROOT, 'dest'), path.join(ROOT, 'dist'),
                   path.join(ROOT, 'test'))


@click.group()
def cli():
    pass


@cli.command(help='Build this package')
@click.argument('names', nargs=-1)
@click.option('--clear', is_flag=True, help='Clear build files')
def build(names, clear):
    if clear:
        pkg_build_clear(pkg_spec)
    else:
        pkg_build(pkg_spec)


@cli.command(help='Pack into package')
@click.option('--clear', is_flag=True, help='Clear distribution files')
def dist(clear):
    if clear:
        pkg_dist_clear(pkg_spec)
    else:
        pkg_dist(pkg_spec)


@cli.command(help='Run unit tests')
def test():
    pkg_test(pkg_spec)


cli()
