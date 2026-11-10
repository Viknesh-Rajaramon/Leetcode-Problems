from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        result, step_1, step_0 = 0, 0, 0
        for cost in costs:
            step_0, step_1, result = step_1, result, cost + min(step_0+9, step_1+4, result+1)
        
        return result
