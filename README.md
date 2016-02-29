lru-cache
=========

A least recently used (LRU) cache implemented in python.

Installation
------------

Make sure you have `python3` installed and in your PATH.

Install sortedcontainers for python3. (`pip3 install sortedcontainers`)

Information
-----------

`LRUCache.READ` mode has `O(1)` get, `O(1)` set (not full), and `O(n)` set (full)

`LRUCache.WRITE` mode has `O(log n)` get, and `O(log n)` set.

Getting a key that does not exist will return `None`.

Usage
-----

Import LRUCache from lru_cache.py

Create a LRUCache, passing in size (int) and mode (`LRUCache.READ` or `LRUCache.WRITE`)

Call `.get` and `.set` on the cache as desired, passing in the key first, and the value second (only for set).

Testing
-------

Execute lru_cache.py. (`./lru_cache.py`)

Input integer representing desired size.

Input whether you want a read optimized or write optimized cache.

Submit actions of one of the following forms:

* get \<enter\> (key: no quotes) \<enter\>

* set \<enter\> (key: no quotes) \<enter\> (value: eval'd, so quotes necessary for string) \<enter\>

CTRL-C when done.
