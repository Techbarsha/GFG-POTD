class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        # This code implemented by Barsha Saha
        if len(s1) != len(s2):
            return False
        
        map1 = {}
        map2 = {}
        
        for c1, c2 in zip(s1, s2):
            
            # Check mapping from s1 to s2
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2
            
            # Check reverse mapping from s2 to s1
            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1
        
        return True
        
        
