from imports import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        volume = 0

        while i <= j:
            new_volume = (j-i) * min(height[i], height[j])
            if new_volume >= volume:
                volume = new_volume
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return volume
