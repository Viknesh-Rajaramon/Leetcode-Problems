from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        deletion_cost = defaultdict(int)
        for i, c in enumerate(s):
            deletion_cost[c] += cost[i]

        return sum(deletion_cost.values()) - max(deletion_cost.values())
