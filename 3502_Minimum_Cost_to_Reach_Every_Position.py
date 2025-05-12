from imports import *

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        min_cost = cost[0]
        ans = [cost[0]]
        for i in range(1, len(cost)):
            min_cost = min(min_cost, cost[i])
            ans.append(min_cost)

        return ans
