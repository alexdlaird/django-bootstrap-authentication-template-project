"""
The file below is used in place of the common Django settings file, and instead this file
determines the settings file to use depending on the environment. For instance, one settings
file may be used in development, one in production. Two separate settings files may define
settings specific to their environment, but they both may also share common settings attributes.

This settings file first loads the "common" settings file, then loads the settings file specific
to the environment being run in.
"""

# Import system modules
import socket
import sys

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

common_conf_module = __import__('conf.configs.common', globals(), locals(), 'myproject')

# Load common conf properties into the local scope
for setting in dir(common_conf_module):
    if setting == setting.upper():
        locals()[setting] = getattr(common_conf_module, setting)

# The default assumption is that we're not testing, but if the testing environment is deteched, this value will change
TESTING = False

# Assume we are not in a production environment until that configuration environment is loaded, which is crucial to
# prevent certain functionality (for instance, subscriptions) from ever firing outside of a production environment
IS_PRODUCTION = False

if 'test' not in sys.argv:
    # Available environments for conf files are keyed by hostname
    confs = {
        'm.host.com': 'prod',
    }

    # If the hostname is not in the list of confs, use 'dev' conf
    HOSTNAME = socket.gethostname()
    conf_module = __import__('conf.configs.%s' % (confs[HOSTNAME] if HOSTNAME in confs.keys() else 'dev'),
                             globals(),
                             locals(), 'myproject')
    
    # If we're in our production environment, set the flag
    if HOSTNAME in confs.keys() and confs[HOSTNAME] == 'prod':
        IS_PRODUCTION = True

    # Load the conf properties into the local scope
    for setting in dir(conf_module):
        if setting == setting.upper():
            locals()[setting] = getattr(conf_module, setting)
# If we're running tests, run a streamlined settings file for efficiency
else:
    TESTING = True

    test_conf_module = __import__('conf.configs.test', globals(), locals(), 'myproject')

    # Load test conf properties into the local scope
    for setting in dir(test_conf_module):
        if setting == setting.upper():
            locals()[setting] = getattr(test_conf_module, setting)

# Last things last, load environment variables from this file into the scope
locals()['TESTING'] = TESTING
locals()['IS_PRODUCTION'] = IS_PRODUCTION
locals()['HOSTNAME'] = HOSTNAME