import threading
from Cache import Cache

class MultiLevelCache:
    def __init__(self):
        self.cache_levels = []
        self.lock = threading.Lock()

    def add_cache_level(self, size: int, eviction_policy: str):
        with self.lock:
            self.cache_levels.append(Cache(size, eviction_policy))

    def remove_cache_level(self, level: int):
        with self.lock:
            if 0 <= level < len(self.cache_levels):
                del self.cache_levels[level]

    def get(self, key: str) -> str:
        with self.lock:
            # Check from highest priority (L1) to lowest (Ln)
            for i, cache in enumerate(self.cache_levels):
                result = cache.get(key)
                if result is not None:
                    # Promote the item to L1
                    for j in range(i, 0, -1):
                        self.cache_levels[j - 1].put(key, result)
                    return result
            return None  # Cache miss

    def put(self, key: str, value: str):
        with self.lock:
            if self.cache_levels:
                # Always insert into L1
                self.cache_levels[0].put(key, value)

    def _handle_promotion(self, key: str, value: str):
        for i in range(1, len(self.cache_levels)):
            if self.cache_levels[i].get(key) is not None:
                self.cache_levels[i - 1].put(key, value)
                self.cache_levels[i].remove(key)  # Remove from lower level
                return

    def display_cache(self):
        for i, cache in enumerate(self.cache_levels):
            print(f"L{i+1} Cache:")
            cache.display()
