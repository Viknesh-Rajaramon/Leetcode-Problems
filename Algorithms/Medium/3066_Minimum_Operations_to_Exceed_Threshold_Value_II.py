from imports import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        x  = heappop(nums)

        while x < k:
            new_val = x*2 + heappop(nums)
            x = heappushpop(nums, new_val)
            count += 1
        
        return count
