from imports import *

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        class FenwickTree:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n+1)

            def add(self, i: int, v: int) -> None:
                i += 1
                while i <= self.n:
                    self.bit[i] += v
                    i += i & -i

            def _sum(self, i: int):
                i += 1
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i

                return s

            def range_sum(self, l: int, r: int) -> int:
                if l > r:
                    return 0

                return self._sum(r) - self._sum(l-1)

        n, s = len(s), list(s)
        ft = FenwickTree(n)
        for i in range(1, n):
            if s[i] != s[i-1]:
                ft.add(i, 1)

        result = []
        for q in queries:
            if q[0] == 1:
                j = q[1]
                if j > 0:
                    old = 1 if s[j] != s[j-1] else 0

                if j + 1 < n:
                    old2 = 1 if s[j+1] != s[j] else 0

                s[j] = "A" if s[j] == "B" else "B"

                if j > 0:
                    new = 1 if s[j] != s[j-1] else 0
                    ft.add(j, new - old)

                if j+1 < n:
                    new2 = 1 if s[j+1] != s[j] else 0
                    ft.add(j+1, new2 - old2)
            else:
                if q[1] == q[2]:
                    result.append(0)
                else:
                    result.append(q[2] - q[1] - ft.range_sum(q[1]+1, q[2]))

        return result
