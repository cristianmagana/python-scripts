from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        
        # key -> value mapping
        self.key_to_val = {}
        
        # key -> frequency mapping
        self.key_to_freq = {}
        
        # frequency -> OrderedDict of keys (maintains insertion/access order)
        # OrderedDict handles LRU within same frequency
        self.freq_to_keys = defaultdict(OrderedDict)
    
    def get(self, key):
        """Get value and update frequency"""
        if key not in self.key_to_val:
            return -1
        
        # Update frequency
        self._update_freq(key)
        
        return self.key_to_val[key]
    
    def put(self, key, value):
        """Put key-value pair"""
        if self.capacity <= 0:
            return
        
        # Update existing key
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return
        
        # Add new key - check capacity
        if len(self.key_to_val) >= self.capacity:
            self._evict()
        
        # Insert new key
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None  # Value doesn't matter, we just need the key
        self.min_freq = 1
    
    def _update_freq(self, key):
        """Increment frequency of a key"""
        freq = self.key_to_freq[key]
        
        # Remove from current frequency list
        del self.freq_to_keys[freq][key]
        
        # If this was the only key at min_freq and we removed it, increment min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        # Add to next frequency list
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None
    
    def _evict(self):
        """Remove least frequently used key (and LRU if tie)"""
        # Get the LRU key from min_freq bucket
        # OrderedDict's first key is the least recently used
        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        
        # Remove from all mappings
        del self.key_to_val[key]
        del self.key_to_freq[key]

# Usage
cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1, freq of key 1 becomes 2

cache.put(3, 3)           # evicts key 2 (freq=1, LRU)
print(cache.get(2))       # returns -1 (not found)

print(cache.get(3))       # returns 3, freq of key 3 becomes 2
cache.put(4, 4)           # evicts key 1 (both have freq=2, but 1 is LRU)
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4