from imports import *

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        arr = sorted([abs(num) for num in nums])
        result = 0        
        n, l = len(arr), 0
        for r in range(n):
            while arr[r] > arr[l]*2:
                l += 1
            
            result += r-l
        
        return result
