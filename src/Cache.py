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