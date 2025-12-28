from functools import lru_cache

class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def count_balanced_nums(num: int) -> int:
            s = str(num)
            n = len(s)

            @lru_cache(None)
            def dp(pos: int, diff: int, tight: bool, started: bool, length: int) -> int:
                if pos == n:
                    return 1 if started and length >= 2 and diff == 0 else 0

                result, limit = 0, int(s[pos]) if tight else 9
                for d in range(limit+1):
                    new_tight = tight and (d == limit)
                    if not started and d == 0:
                        result += dp(pos+1, diff, new_tight, False, 0)
                        continue

                    new_diff = diff + d if length % 2 == 0 else diff - d
                    result += dp(pos+1, new_diff, new_tight, True, length+1)

                return result

            return dp(0, 0, True, False, 0)
        
        return count_balanced_nums(high) - count_balanced_nums(low-1)
