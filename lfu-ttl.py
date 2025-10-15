from collections import defaultdict, OrderedDict
import time

class LFUCacheWithTTL:
    def __init__(self, capacity, ttl_seconds=60):
        self.capacity = capacity
        self.ttl_seconds = ttl_seconds
        self.min_freq = 0
        
        self.key_to_val = {}
        self.key_to_freq = {}
        self.key_to_timestamp = {}  # Track when items were added
        self.freq_to_keys = defaultdict(OrderedDict)
    
    def get(self, key):
        if key not in self.key_to_val:
            return -1
        
        # Check if expired
        if time.time() - self.key_to_timestamp[key] > self.ttl_seconds:
            self._remove(key)
            return -1
        
        self._update_freq(key)
        return self.key_to_val[key]
    
    def put(self, key, value):
        if self.capacity <= 0:
            return
        
        # Update existing
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self.key_to_timestamp[key] = time.time()
            self._update_freq(key)
            return
        
        # Add new - evict if needed
        if len(self.key_to_val) >= self.capacity:
            self._evict()
        
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.key_to_timestamp[key] = time.time()
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
    
    def _update_freq(self, key):
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None
    
    def _evict(self):
        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        self._remove(key)
    
    def _remove(self, key):
        """Helper to remove a key completely"""
        if key in self.key_to_val:
            freq = self.key_to_freq[key]
            del self.freq_to_keys[freq][key]
            del self.key_to_val[key]
            del self.key_to_freq[key]
            del self.key_to_timestamp[key]

# Usage
cache = LFUCacheWithTTL(capacity=2, ttl_seconds=5)

cache.put(1, "one")
cache.put(2, "two")
print(cache.get(1))  # "one"

time.sleep(6)
print(cache.get(1))  # -1 (expired)
```

---

## Visual Example - How LFU Works
```
Initial state: capacity=2, cache is empty
freq_to_keys = {}

put(1, "A"):
freq_to_keys = {1: {1: None}}
min_freq = 1

put(2, "B"):
freq_to_keys = {1: {1: None, 2: None}}
min_freq = 1

get(1):  # Access key 1
freq_to_keys = {1: {2: None}, 2: {1: None}}
min_freq = 1

put(3, "C"):  # Evicts key 2 (freq=1, LRU)
freq_to_keys = {1: {3: None}, 2: {1: None}}
min_freq = 1