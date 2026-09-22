from math import inf

class Solution:
    def minOperations(self, s: str) -> int:
        result, n = inf, len(s)
        for k in range(n):
            ops = k
            for i in range(n//2):
                inc = abs(ord(s[(k+i) % n]) - ord(s[(n+k-1-i) % n]))
                ops += min(inc, 26 - inc)

            result = min(result, ops)

        return result
