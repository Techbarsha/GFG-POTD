class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        count = 1
        max_height = height[0]
        
        for i in range(1, len(height)):
        
            if height[i] > max_height:
                count += 1
                max_height = height[i]
        
        return count
