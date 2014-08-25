"""
Django settings.
"""

# Import system modules
import socket
import sys

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

common_conf_module = __import__('conf.common', globals(), locals(), 'myproject')

# Load common conf properties into the local scope
for setting in dir(common_conf_module):
    if setting == setting.upper():
        locals()[setting] = getattr(common_conf_module, setting)

if 'test' not in sys.argv:
    # Available environments for conf files are keyed by hostname
    confs = {
        'prod.host.com': 'prod',
    }

    # If the hostname is not in the list of confs, use 'dev' conf
    hostname = socket.gethostname()
    conf_module = __import__('conf.%s' % (confs[hostname] if hostname in confs.keys() else 'dev'),
                             globals(),
                             locals(), 'myproject')

    # Load the conf properties into the local scope
    for setting in dir(conf_module):
        if setting == setting.upper():
            locals()[setting] = getattr(conf_module, setting)
# If we're running tests, run a streamlined settings file for efficiency
else:
    test_conf_module = __import__('conf.test', globals(), locals(), 'myproject')

    # Load test conf properties into the local scope
    for setting in dir(test_conf_module):
        if setting == setting.upper():
            locals()[setting] = getattr(test_conf_module, setting)