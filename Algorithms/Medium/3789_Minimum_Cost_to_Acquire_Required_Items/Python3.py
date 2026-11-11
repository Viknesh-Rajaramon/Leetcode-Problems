class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost_a = need1*cost1 + need2*cost2
        cost_b = min(need1, need2) * (costBoth - cost1 - cost2)
        cost_c = max(need1, need2) * costBoth
        return min(cost_a + min(0, cost_b), cost_c)
