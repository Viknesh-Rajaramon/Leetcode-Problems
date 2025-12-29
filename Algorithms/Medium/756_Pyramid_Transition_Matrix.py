from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        blocks = {}
        for triple in allowed:
            blocks.setdefault(triple[:2], []).append(triple[2])

        memo = {}
        def dfs(row):
            if row in memo:
                return memo[row]
            
            if len(row) == 1:
                memo[row] = True
                return True
            
            n = len(row)
            for i in range(n - 1):
                if row[i : i+2] not in blocks:
                    memo[row] = False
                    return False
            
            def helper(i, curr):
                if i == n - 1:
                    return dfs(curr)
                
                for c in blocks.get(row[i : i+2], []):
                    if helper(i+1, curr+c):
                        return True
                
                return False
            
            memo[row] = helper(0, "")
            return memo[row]
        
        return dfs(bottom)
