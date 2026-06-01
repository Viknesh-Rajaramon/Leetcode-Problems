from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        result, n = 0, len(cost)
        for i in range(0, n, 3):
            result += cost[i] + (cost[i+1] if i+1 < n else 0)

        return result
