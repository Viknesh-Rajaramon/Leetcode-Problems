from imports import *

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        
        bob_visited_time = {}
        def dfs_bob(node, parent, time) -> bool:
            if node == 0:
                bob_visited_time[node] = time
                return True
            
            for e in graph[node]:
                if e != parent and dfs_bob(e, node, time+1):
                    bob_visited_time[node] = time
                    return True

            return False

        dfs_bob(bob, -1, 0)
        
        def dfs_alice(node, parent, time):
            max_amount = -inf

            for e in graph[node]:
                if e != parent:
                    max_amount = max(max_amount, dfs_alice(e, node, time + 1))
            
            node_income = 0
            if node in bob_visited_time and bob_visited_time[node] < time:
                node_income = 0
            elif node in bob_visited_time and bob_visited_time[node] == time:
                node_income = amount[node] // 2
            else:
                node_income = amount[node]
            
            if max_amount == -inf:
                return node_income
            
            return max_amount + node_income

        return dfs_alice(0, -1, 0)
