from imports import *

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        val, dp = [1 if x == 1 else -1 for x in good], [0] * n
        def bottom_up_dp(node: int, parent: int) -> None:
            dp[node] = val[node]
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                
                bottom_up_dp(neighbor, node)
                dp[node] += max(0, dp[neighbor])
        
        result = [0] * n
        def top_down_dp(node: int, parent: int, par: int) -> None:
            result[node] = dp[node] + par
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                
                child_par = max(0, result[node] - max(0, dp[neighbor]))
                top_down_dp(neighbor, node, child_par)
        
        bottom_up_dp(0, -1)
        top_down_dp(0, -1, 0)
        return result
