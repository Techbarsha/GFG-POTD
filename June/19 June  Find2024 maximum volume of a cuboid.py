import math

class Solution:
    def maxVolume(self, perimeter: float, area: float) -> float:
        ans = (math.pow((perimeter - (math.sqrt(math.pow(perimeter, 2) - (24 * area)))) / 12, 2) *
               ((perimeter / 4) -
                (2 * ((perimeter - (math.sqrt(math.pow(perimeter, 2) - (24 * area)))) / 12))))

        return ans
