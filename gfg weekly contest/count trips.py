
import math

class Solution:

    def countTrips(self, locations):
        # code here
        uniqueAngles = set()
        for loc in locations:
            x, y = loc
            if x != 0 or y != 0:
                angle = math.atan2(y, x)
                uniqueAngles.add(angle)

        return len(uniqueAngles)
