'''
SYNOPSIS

    class ThemeNotSpecifyError
    class ThemeNotFoundError
    class MissingStepError

DESCRIPTION

    Specific error components.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''


class MissingUnitError(Exception):
    def __init__(self, path, name):
        self._msg = "path=%s, name=%s" % (path, name)

    def __str__(self):
        return self._msg


class ThemeNotSpecifyError(Exception):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ThemeNotFoundError(Exception):
    def __init__(self, name):
        self.error = 'Not found theme {}'.format(name)

    def __str__(self):
        return self.error


class MissingStepError(Exception):
    def __init__(self, step_name):
        self._step_name = step_name

    def __str__(self):
        return self._step_name
