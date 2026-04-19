from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n-2):
            if not nums[i]:
                nums[i] = not nums[i]
                nums[i+1] = not nums[i+1]
                nums[i+2] = not nums[i+2]
                count += 1
        
        if not nums[i+1] or not nums[i+2]:
            return -1
        
        return count
