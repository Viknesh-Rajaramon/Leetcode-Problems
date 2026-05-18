from typing import List
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        

        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)
        
        result, curr, visited = 0, [0], set([0])
        while curr:
            nxt = []
            for node in curr:
                if node == n-1:
                    return result
                
                for child in graph[arr[node]]:
                    if child not in visited:
                        nxt.append(child)
                        visited.add(child)
                    
                graph[arr[node]].clear()
                for child in [node-1, node+1]:
                    if 0 <= child < n and child not in visited:
                        nxt.append(child)
                        visited.add(child)
            
            curr = nxt
            result += 1

        return -1
