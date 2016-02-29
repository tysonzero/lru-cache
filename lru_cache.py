#!/usr/bin/env python3

from sortedcontainers import SortedListWithKey


class LRUCache:
    READ = 'read'  # O(1) get / O(n) set
    WRITE = 'write'  # O(log n) get / O(log n) set

    def __init__(self, size, mode):
        self._size = size
        self._mode = mode
        self._cache = {}
        self._used = {}
        if mode == self.READ:
            self._time = 0
        elif mode == self.WRITE:
            self._times = SortedListWithKey(key=self._used.get)

    def _use(self, key):
        if self._mode == self.READ:
            self._used[key] = self._time
            self._time += 1
        elif self._mode == self.WRITE:
            if self._times:
                if key in self._used:
                    self._times.discard(key)
                self._used[key] = self._used[self._times[-1]] + 1
            else:
                self._used[key] = 0
            self._times.add(key)

    def _remove(self):
        if self._mode == self.READ:
            lru = min(self._used, key=self._used.get)
            del self._cache[lru]
            del self._used[lru]
        elif self._mode == self.WRITE:
            lru = self._times.pop(0)
            del self._cache[lru]
            del self._used[lru]

    def get(self, key):
        item = self._cache.get(key)
        if item is None:
            return None
        self._use(key)
        return item

    def set(self, key, value):
        if key not in self._cache:
            if len(self._cache) == self._size:
                self._remove()
        self._cache[key] = value
        self._use(key)

    def __repr__(self):
        return repr(self._cache)


if __name__ == '__main__':
    size = int(input('Size: '))
    mode = None
    while mode not in ['read', 'write']:
        mode = input('read or write heavy?: ')
    lru = LRUCache(size, mode)
    while True:
        action = None
        while action not in ['get', 'set']:
            action = input('get or set: ')
        key = input('key: ')
        if action == 'get':
            print(lru.get(key))
        elif action == 'set':
            value = eval(input('value: '))
            lru.set(key, value)
        print(lru)

