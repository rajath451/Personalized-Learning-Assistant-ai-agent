# src/memory/memory_bank.py

class MemoryBank:
    def __init__(self):
        self._store = {}

    def add(self, key, value):
        self._store[key] = value

    def get(self, key, default=None):
        return self._store.get(key, default)

    def remove(self, key):
        if key in self._store:
            del self._store[key]