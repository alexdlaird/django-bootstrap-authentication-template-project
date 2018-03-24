import re

from django.core.cache.backends.locmem import LocMemCache

__author__ = "Alex Laird"
__copyright__ = "Copyright 2018, Alex Laird"
__version__ = '0.2.0'


class LocMemKeysCache(LocMemCache):
    def keys(self, search):
        pattern = re.compile(self.make_key(search))

        keys = []
        with self._lock.reader():
            for key, value in self._cache.items():
                if pattern.match(key):
                    keys.append(key.lstrip(':' + str(self.version)).lstrip(':' + str(self.key_prefix)))

        return keys
