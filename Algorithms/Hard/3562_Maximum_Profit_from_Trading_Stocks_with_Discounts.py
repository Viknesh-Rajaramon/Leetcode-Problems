from typing import List, Tuple
from collections import defaultdict

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = defaultdict(list)
        for u, v in hierarchy:
            graph[u-1].append(v-1)
        
        def dfs(u: int) -> Tuple[List[int], List[int], int]:
            cost, discount_cost = present[u], present[u] // 2, 
            dp_0, dp_1 = [0] * (budget+1), [0] * (budget+1)
            sub_profit_0, sub_profit_1, u_size = [0] * (budget+1), [0] * (budget+1), cost
            
            for v in graph[u]:
                child_dp_0, child_dp_1, v_size = dfs(v)
                u_size += v_size
                for i in range(budget, -1, -1):
                    for sub in range(min(v_size, i) + 1):
                        if i >= sub:
                            sub_profit_0[i] = max(
                                sub_profit_0[i], sub_profit_0[i-sub] + child_dp_0[sub]
                            )
                            sub_profit_1[i] = max(
                                sub_profit_1[i], sub_profit_1[i-sub] + child_dp_1[sub]
                            )

            for i in range(budget+1):
                dp_0[i], dp_1[i] = sub_profit_0[i], sub_profit_0[i]
                if i >= discount_cost:
                    dp_1[i] = max(sub_profit_0[i], sub_profit_1[i-discount_cost] + future[u] - discount_cost)
                
                if i >= cost:
                    dp_0[i] = max(sub_profit_0[i], sub_profit_1[i-cost] + future[u] - cost)

            return dp_0, dp_1, u_size

        return dfs(0)[0][budget]
