from collections import OrderedDict
from pprint import pprint as pp # this is used for display purpose only

class LRUcache:

    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    # Check if key is present in cache.
    # If not present return -1
    # Updated the order of the accessed item if present
    def get(self,key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    # Update value and move to end
    # If capacity is reached discard first item
    # in LRU since we are moving everything to end
    def put(self,key,value):
         self.cache[key] = value
         self.cache.move_to_end(key)
         if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Testing
cache = LRUcache(5)
cache.put(34,"John")
cache.put(43,"Mary")
cache.put(23,"Jack")
cache.put(67,"Jill")
cache.put(54,"Peter")

# Display the cache
pp(cache.cache)

# Fetch an element , catch hit and print whats happening in cache order
result = cache.get(23)
pp(cache.cache)
print(result)

# Fetch an element , catch miss and print whats happening in cache order
result = cache.get(99)
pp(cache.cache)
print(result)

# Test cache eviction by inserting a new element
cache.put(77,"Abby")
pp(cache.cache)