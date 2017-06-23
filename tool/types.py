'''
SYNOPSIS

    class Version
    class PkgSpec
    class ThemeSpec

DESCRIPTION

    Common types used in tool.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''


class Version:
    def __init__(self, major, minor, rev=0, deb_rev=0):
        self._major = major
        self._minor = minor
        self._rev = rev
        self._pkg_ver = '{}.{}.{}'.format(major, minor, rev)
        self._deb_rev = deb_rev
        self._deb_ver = '{}-{}'.format(self._pkg_ver, deb_rev)

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def rev(self):
        return self._rev

    @property
    def pkg_ver(self):
        return self._pkg_ver

    @property
    def deb_rev(self):
        return self._deb_rev

    @property
    def deb_ver(self):
        return self._deb_ver


class PkgSpec:
    def __init__(self, name, version, root, src, dest, dist, test):
        self._name = name
        self._deb_name = '{}_{}'.format(name, version.deb_ver)
        self._version = version
        self._root = root
        self._src = src
        self._dest = dest
        self._dist = dist
        self._test = test

    @property
    def name(self):
        return self._name

    @property
    def deb_name(self):
        return self._deb_name

    @property
    def version(self):
        return self._version

    @property
    def root(self):
        return self._root

    @property
    def src(self):
        return self._src

    @property
    def dest(self):
        return self._dest

    @property
    def dist(self):
        return self._dist

    @property
    def test(self):
        return self._test


class ThemeSpec(object):
    def __init__(self, name, front_color, back_color, danger_color):
        self._name = name
        self._front_color = front_color
        self._back_color = back_color
        self._danger_color = danger_color

    @property
    def name(self):
        return self._name

    @property
    def front_color(self):
        return self._front_color

    @property
    def back_color(self):
        return self._back_color

    @property
    def danger_color(self):
        return self._danger_color
