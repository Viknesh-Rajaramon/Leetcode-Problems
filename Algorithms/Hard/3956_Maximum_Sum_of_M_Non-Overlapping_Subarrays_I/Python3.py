from typing import List
from math import inf
from collections import deque

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        result, dp = -inf, [0] * (n+1)
        for i in range(1, m+1):
            queue, new_dp = deque(), [-inf] * (n+1)
            for j in range(l*i, n+1):
                k = j-l
                curr_val = dp[k] - prefix[k]
                while queue and queue[-1][0] <= curr_val:
                    queue.pop()
                    
                queue.append((curr_val, k))
                
                if queue[0][1] < j-r:
                    queue.popleft()
                
                new_dp[j] = max(new_dp[j-1], queue[0][0] + prefix[j])
            
            result = max(result, new_dp[n])
            dp = new_dp

        return result
