from typing import List

class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp_0, dp_1 = 0, nums[0]
        for i in range(1, n):
            if colors[i-1] == colors[i]:
                new_dp_1 = dp_0 + nums[i]
                new_dp_0 = max(dp_0, dp_1)
            else:
                new_dp_0 = max(dp_0, dp_1)
                new_dp_1 = max(dp_0, dp_1) + nums[i]
            
            dp_0, dp_1 = new_dp_0, new_dp_1

        return max(dp_0, dp_1)
