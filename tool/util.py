'''
SYNOPSIS

    real_theme_name(short_name)
    short_theme_name(name)

DESCRIPTION

    Utilities are use in tools.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''


def real_theme_name(short_name):
    return 'venom-{}'.format(short_name)


def short_theme_name(name):
    return name[len('venom-'):]
