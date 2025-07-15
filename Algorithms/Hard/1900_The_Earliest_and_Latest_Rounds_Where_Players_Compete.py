from imports import *

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def dp(n: int, p1: int, p2: int) -> Tuple[int, int]:
            if p1 == p2:
                return (1, 1)
            
            if p1 > p2:
                p1, p2 = p2, p1
            
            min_round, max_round = inf, -inf
            for i in range(1, p1 + 1):
                for j in range(p1 - i + 1, p2 - i + 1):
                    m = (n + 1) // 2
                    if p1 + p2 - n // 2 <= i + j <= m:
                        x, y = dp(m, i, j)
                        min_round = min(min_round, x)
                        max_round = max(max_round, y)
            
            return (min_round + 1, max_round + 1)

        return list(dp(n, firstPlayer, n - secondPlayer + 1))
