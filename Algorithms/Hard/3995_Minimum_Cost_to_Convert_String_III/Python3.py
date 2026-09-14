from math import inf

class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        dp = [-1] * (n+1)
        def f(i: int) -> int:
            if i == n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            result = inf
            if source[i] == target[i]:
                result = f(i+1)
            
            for j in range(len(rules)):
                x, y = rules[j]
                if i + len(x) > n:
                    continue
                
                valid, wildcard = True, 0
                for k in range(len(x)):
                    if x[k] != '*' and source[i+k] != x[k]:
                        valid = False
                        break
                    
                    if x[k] == '*':
                        wildcard += 1
                    
                    if y[k] != target[i+k]:
                        valid = False
                        break

                if not valid:
                    continue
                
                nxt = f(i + len(x))
                if nxt != inf:
                    result = min(result, costs[j] + wildcard + nxt)

            dp[i] = result
            return result
        
        result = f(0)
        return result if result != inf else -1
