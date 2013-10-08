
import sys
import os

def get():
    config_file = os.path.expanduser('~/.tweeter_config')
    if not os.path.exists(config_file):
        sys.stderr.write('Can not find config file')
        raise
    config = {}
    execfile(config_file, config)
    return config
