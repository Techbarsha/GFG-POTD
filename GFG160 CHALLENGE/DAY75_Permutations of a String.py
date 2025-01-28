from itertools import permutations
class Solution:
    def findPermutation(self, s):
        # Code here
        unique_permutations = set(permutations(s))
        return [''.join(p) for p in unique_permutations]
