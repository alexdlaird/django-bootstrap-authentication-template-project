__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import re

from django.core.cache.backends.locmem import LocMemCache


class LocMemKeysCache(LocMemCache):
    """
    Extends the generic in-memory cache to support the querying of keys, similar to how a Redis-based implementation
    might similar support this.
    """

    def keys(self, search):
        pattern = re.compile(self.make_key(search))

        keys = []
        for key, value in self._cache.items():
            if pattern.match(key):
                keys.append(key.lstrip(':' + str(self.version)).lstrip(':' + str(self.key_prefix)))

        return keys
