from typing import List
from collections import defaultdict

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in swaps:
            graph[u].append(v)
            graph[v].append(u)
        
        visited, result = set(), 0
        for i in range(len(nums)):
            if i in visited:
                continue
            
            idx, val = [], []
            st = [i]
            visited.add(i)

            while st:
                c = st.pop()
                idx.append(c)
                val.append(nums[c])
                for x in graph[c]:
                    if x not in visited:
                        visited.add(x)
                        st.append(x)
            
            val.sort(reverse = True)
            even, odd = 0, 0
            for x in idx:
                if x % 2 == 0:
                    even += 1
                else:
                    odd += 1
                    
            p = 0
            for _ in range(even):
                result += val[p]
                p += 1
            
            for _ in range(odd):
                result -= val[p]
                p += 1
            
        return result
