class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        def solve(num: int) -> int:
            s, dp = str(num), {}
            def dfs(i: int, p: int, tight: bool, started: bool) -> int:
                if i == len(s):
                    return 1 if started else 0
                
                key = (i, p, tight, started)
                if key in dp:
                    return dp[key]
                
                result, limit = 0, int(s[i]) if tight else 9
                for d in range(limit+1):
                    if p == -1 and d == 0:
                        result += dfs(i+1, -1, tight and d == limit, False)
                    elif p == -1 or abs(p-d) <= k:
                        result += dfs(i+1, d, tight and d == limit, True)
            
                dp[key] = result
                return result
            
            return dfs(0, -1, True, False)
        
        return solve(r) - solve(l-1)
