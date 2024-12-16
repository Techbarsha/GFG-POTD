class Solution:
    def aggressiveCows(self, stalls, k):
        
        stalls.sort()

        # Binary search for the largest minimum distance
        def canPlaceCows(min_dist):
            count = 1
            last_position = stalls[0]

            # Try to place the rest of the cows
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= min_dist:
                    count += 1
                    last_position = stalls[i]
                if count == k:
                    return True
            return False

        # Binary search on the answer(minimum distance)
        low, high = 1, stalls[-1] - stalls[0]
        best_dist = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceCows(mid):
                best_dist = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best_dist
