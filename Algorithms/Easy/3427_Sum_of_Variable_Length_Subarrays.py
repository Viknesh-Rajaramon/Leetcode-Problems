from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        result = 0
        for i in range(n):
            start = max(0, i-nums[i])
            result += prefix_sum[i+1] - prefix_sum[start]
        
        return result
