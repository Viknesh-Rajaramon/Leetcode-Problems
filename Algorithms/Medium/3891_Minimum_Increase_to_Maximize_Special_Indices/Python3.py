from typing import List
from math import inf

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n, dp_0, cost_0, dp_1, cost_1 = len(nums), 0, 0, -inf, inf
        for i in range(1, n-1):
            new_dp_0, new_cost_0 = 0, 0
            if dp_0 > dp_1:
                new_dp_0, new_cost_0 = dp_0, cost_0
            elif dp_0 < dp_1:
                new_dp_0, new_cost_0 = dp_1, cost_1
            else:
                new_dp_0, new_cost_0 = dp_0, min(cost_0, cost_1)
            
            dp_1, cost_1 = dp_0+1, cost_0 + max(0, max(nums[i-1], nums[i+1])+1-nums[i])
            dp_0, cost_0 = new_dp_0, new_cost_0
        
        if dp_0 > dp_1:
            return cost_0
        
        if dp_0 < dp_1:
            return cost_1
        
        return min(cost_0, cost_1)
