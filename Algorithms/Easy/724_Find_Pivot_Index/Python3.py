from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        for i in range(n):
            right_sum = total_sum - prefix_sum[i] - nums[i]
            if prefix_sum[i] == right_sum:
                return i
        
        return -1
