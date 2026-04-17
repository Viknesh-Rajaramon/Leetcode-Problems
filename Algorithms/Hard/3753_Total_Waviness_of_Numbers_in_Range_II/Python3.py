from typing import Optional, Tuple
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def total_waviness_upto(num: int) -> int:
            digits = list(map(int, str(num)))
            n = len(digits)

            @lru_cache(None)
            def dfs(
                pos: int,
                p1: Optional[int],
                p2: Optional[int],
                tight: bool,
                has_started: bool
            ) -> Tuple[int, int]:
                if pos == n:
                    return 0, 1

                max_d, waviness, count = digits[pos] if tight else 9, 0, 0
                for d in range(max_d+1):
                    next_started = has_started or (d != 0)
                    if not next_started:
                        nd1, nd2 = None, None
                    elif not has_started:
                        nd1, nd2 = d, None
                    else:
                        nd1, nd2 = d, p1

                    w, c = dfs(pos+1, nd1, nd2, tight and d == digits[pos], next_started)
                    waviness += w
                    count += c

                    if has_started and next_started and p1 is not None and p2 is not None:
                        if (p2 < p1 > d) or (p2 > p1 < d):
                            waviness += c

                return waviness, count
            
            return dfs(0, None, None, True, False)[0]

        return total_waviness_upto(num2) - total_waviness_upto(num1 - 1)
