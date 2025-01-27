#User function Template for python3

# design the class in the most optimal way

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.cache = {}
        self.capacity = cap
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key not in self.cache : return -1
        val = self.cache[key]
        self.cache.pop(key)
        self.cache[key] = val
        return val
        
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return
        if len(self.cache) == capacity:
            n = -1
            for i in self.cache:
                n = i
                break
            self.cache.pop(n)
            
        self.cache[key] = value
