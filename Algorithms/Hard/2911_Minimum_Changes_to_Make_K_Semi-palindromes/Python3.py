from functools import cache
from operator import ne

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n+1)]
        for i in range(1, n):
            for j in range(2*i, n+1, i):
                divisors[j].append(i)

        @cache
        def peel(i: int, j: int, d: int) -> int:
            if j-i <= d:
                return 0
            
            return sum(map(ne, s[i : i+d], s[j-d : j])) + peel(i+d, j-d, d)

        @cache
        def cost(i: int, j: int) -> int:
            return min(peel(i, j, d) for d in divisors[j-i])

        result = {0: 0}
        for pieces in range(1, k):
            room = range(2*pieces, n - 2*(k - pieces) + 1)
            result = {j: min(result[i] + cost(i, j) for i in result if i <= j-2) for j in room}
        
        return min(result[i] + cost(i, n) for i in result)
