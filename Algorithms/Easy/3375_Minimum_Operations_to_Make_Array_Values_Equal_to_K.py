from imports import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        s = set(nums)
        
        count = 0
        for num in s:
            if num > k:
                count += 1

        return count
