class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost_a = need1*cost1 + need2*cost2
        
        min_need = min(need1, need2)
        cost_b = min_need*costBoth + (need1-min_need)*cost1 + (need2-min_need)*cost2

        cost_c = max(need1, need2) * costBoth

        return min(cost_a, cost_b, cost_c)
