from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        curr_sum = 0

        count = 0
        for i in range(n-1):
            curr_sum += nums[i]
            total -= nums[i]
            if curr_sum >= total:
                count += 1
        
        return count
