from collections import OrderedDict, defaultdict
import threading

class Cache:
    def __init__(self, size: int, eviction_policy: str):
        self.size = size
        self.eviction_policy = eviction_policy
        self.cache = {}
        self.access_order = OrderedDict()
        self.freq_counter = defaultdict(int)
        self.lock = threading.Lock()
    

    def get(self, key: str) -> str:
        with self.lock:
            if key in self.cache:
                if self.eviction_policy == 'LRU':
                    self.access_order.move_to_end(key)
                elif self.eviction_policy == 'LFU':
                    self.freq_counter[key] += 1
                return self.cache[key]
            return None

    def put(self, key: str, value: str):
        with self.lock:
            if key in self.cache:
                self.cache[key] = value
                if self.eviction_policy == 'LRU':
                    self.access_order.move_to_end(key)
                elif self.eviction_policy == 'LFU':
                    self.freq_counter[key] += 1
            else:
                if len(self.cache) >= self.size:
                    self.evict()
                self.cache[key] = value
                if self.eviction_policy == 'LRU':
                    self.access_order[key] = None
                elif self.eviction_policy == 'LFU':
                    self.freq_counter[key] = 1

    def evict(self):
        if self.eviction_policy == 'LRU':
            oldest = next(iter(self.access_order))
            del self.cache[oldest]
            del self.access_order[oldest]
        elif self.eviction_policy == 'LFU':
            least_freq = min(self.freq_counter.values())
            least_frequent_keys = [k for k, v in self.freq_counter.items() if v == least_freq]
            key_to_evict = least_frequent_keys[0]
            del self.cache[key_to_evict]
            del self.freq_counter[key_to_evict]

    def display(self):
        print(f"Cache size: {self.size}, Eviction policy: {self.eviction_policy}")
        for key, value in self.cache.items():
            print(f"{key}: {value}")