'''
SYNOPSIS

    const STAT_DONE
    const STAT_WARN
    const STAT_ERR

    stdlog(stat, action, msg)

DESCRIPTION

    Logging functions.

AUTHORS

    Kevin Leptons <kevin.leptons@gmail.com>
'''

STAT_DONE = 'done'
STAT_WARN = 'warn'
STAT_ERR = 'error'


def stdlog(stat, action, msg):
    '''
    Write log message to stdout

    :param str stat: State of message. It can be successfully, warning or
        error. Use stat_done, stat_warn, stat_err for uniform
    :param str action: Action which perform log
    :param str msg: Message from action
    '''

    print('{} {}: {}'.format(stat, action, msg))
