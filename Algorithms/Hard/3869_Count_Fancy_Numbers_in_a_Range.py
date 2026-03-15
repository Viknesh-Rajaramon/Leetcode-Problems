from functools import lru_cache

class Solution:
    def countFancy(self, l: int, r: int) -> int:
        hs = str(r)
        n = len(hs)
        ls = str(l).zfill(n)

        def check(n: int):
            f1, f2 = 1, 1
            s = str(n)
            for i in range(len(s)-1):
                if s[i+1] <= s[i]:
                    f1 = 0
                
                if s[i+1] >= s[i]:
                    f2 = 0
            
            return f1 or f2

        @lru_cache(None)
        def dp(i: int, lf: int, hf: int, sm: int, f1: int, f2: int, prev: int) -> int:
            if i >= n:
                return 1 if f1 or f2 or check(sm) else 0
            
            result, lw, hi = 0, int(ls[i]) if lf else 0, int(hs[i]) if hf else 9
            for j in range(lw, hi+1):
                tf1 = (prev < j and f1) if sm else 1
                tf2 = (prev > j and f2) if sm else 1
                result += dp(i+1, lf and j == lw, hf and j == hi, sm+j, tf1, tf2, j)

            return result

        return dp(0, 1, 1, 0, 1, 1, 0)
