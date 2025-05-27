from imports import *

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:        
        def intersect(a: List[int], b: List[int]) -> int:
            a = set(a)
            b = set(b)

            return len(a.intersection(b))
        
        n = len(properties)
        visited = set()
        adj_list = [[] for i in range(n)]

        for i in range(n-1):
            for j in range(i+1, n):
                if intersect(properties[i], properties[j]) >= k:
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        print(adj_list)
        
        def dfs(v):
            if v in visited:
                return
            
            visited.add(v)
            for neighbor in adj_list[v]:
                dfs(neighbor)

            return
        
        ans = 0
        for v in range(n):
            if v in visited:
                continue
            
            dfs(v)
            ans += 1
        
        return ans
