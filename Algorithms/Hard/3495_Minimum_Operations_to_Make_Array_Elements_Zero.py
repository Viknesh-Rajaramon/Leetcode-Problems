from imports import *

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for q in queries:
            ops = 0
            prev = 1

            for d in range(1, 17):
                curr = prev * 4
                l = max(q[0], prev)
                r = min(q[1], curr-1)

                if r >= l:
                    ops += (r-l+1) * d
                
                prev = curr
            
            ans += (ops+1) // 2
        
        return ans
