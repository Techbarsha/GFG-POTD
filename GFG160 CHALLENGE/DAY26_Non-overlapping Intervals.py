class Solution:
    def minRemoval(self, intervals):
        # Code here
        
        intervals.sort(key=lambda x: x[1])
        prev_end = float('-inf')
        removals = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1

        return removals
