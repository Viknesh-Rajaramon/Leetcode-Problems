from imports import *

class Solution:
    def rotatedDigits(self, n: int) -> int:
        num = list(map(int, str(n)))
        
        @cache
        def dp(i: int, strict: bool, good: bool) -> int:
            if i == len(num):
                return int(good)
            
            result = 0
            bound = num[i] if strict else 10
            for d in [0, 1, 8]:
                if d < bound:
                    result += dp(i+1, False, good)
                elif d == bound:
                    result += dp(i+1, True, good)
            
            for d in [2, 5, 6, 9]:
                if d < bound:
                    result += dp(i+1, False, True)
                elif d == bound:
                    result += dp(i+1, True, True)
            
            return result
            
        return dp(0, True, False)
