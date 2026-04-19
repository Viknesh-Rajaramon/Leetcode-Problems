from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        result, stack = 0, [(0, 0)]
        for cost, cap in sorted([co, ca] for co, ca in zip(costs, capacity)):
            if cost >= budget:
                break
            
            remaining_budget = budget - cost
            while stack and stack[-1][0] >= remaining_budget:
                stack.pop()
            
            if stack:
                result = max(result, stack[-1][1] + cap)
            
            if not stack or stack[-1][1] < cap:
                stack.append((cost, cap))

        return result
