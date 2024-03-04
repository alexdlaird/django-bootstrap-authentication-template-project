#!/usr/bin/env python
"""
Management script for Django environment.
"""

__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
