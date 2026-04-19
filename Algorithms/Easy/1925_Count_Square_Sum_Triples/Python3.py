from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for a in range(1, n):
            for b in range(a+1, n):
                c = sqrt(a**2 + b**2)
                if int(c) == c and c <= n:
                    result += 2

        return result
