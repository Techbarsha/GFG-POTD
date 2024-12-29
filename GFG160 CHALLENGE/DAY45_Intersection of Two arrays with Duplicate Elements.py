class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        
        # Convert both arrays to sets to remove duplicates
        set_a = set(a)
        set_b = set(b)
        
        # Find intersection of both sets
        intersection = list(set_a.intersection(set_b))
        
        return intersection
