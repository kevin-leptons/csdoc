'''
SYNOPSIS

    pkg_build(spec)
    pkg_build_clear(spec)
    pkg_dist(spec)
    pkg_dist_clear(spec)
    pkg_test(spec)

DESCRIPTION

    Building functions.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''

from os import path
from collections import OrderedDict

from .error import ThemeNotSpecifyError
from .man_builder import build_manpage
from .csdoc_builder import build_csdoc
from .packaging import pack_debian
from .util import real_theme_name
from .shell import rm, call
from .types import ThemeSpec

def pkg_build_clear(spec):
    rm(spec.dest)


def pkg_build(spec):
    # build man page
    build_manpage(spec)

    # build csdoc
    build_csdoc(spec)


def pkg_dist_clear(spec):
    rm(spec.dist)


def pkg_dist(spec):
    pack_debian(spec)


def pkg_test(spec):
    call(['pytest', spec.test])
