from imports import *

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m+1))

        result = []
        for q in queries:
            for i in range(m):
                if q == p[i]:
                    result.append(i)
                    n = p.pop(i)
                    p.insert(0, n)
                    break
        
        return result
