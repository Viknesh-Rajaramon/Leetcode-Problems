from math import inf

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        def solve(req: list[int]) -> int:
            n = len(req)
            dp = [0] * (n+2)
            for _ in range(k):
                new = [inf] * (n+2)
                for i in range(n-1, -1, -1):
                    new[i] = min(new[i+1], req[i] + dp[i+2])

                dp = new
            
            return dp[0]
        
        n = len(nums)
        if k > n//2:
            return -1
        
        req = [0] * n
        for i, num in enumerate(nums):
            prev, nxt = nums[i-1] if i > 0 else nums[-1], nums[i+1] if i < n-1 else nums[0]
            req[i] = max(0, max(prev, nxt) + 1 - num)

        return min(solve(req[ : -1] + [inf]), solve([inf] + req[1 : ]))
