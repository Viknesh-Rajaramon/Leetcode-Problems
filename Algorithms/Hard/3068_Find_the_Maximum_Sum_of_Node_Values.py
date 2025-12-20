from typing import List
from math import inf

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[-1] * 2 for _ in range(n)]

        def maxSumOfNodes(index: int, isEven: bool):
            if index == n:
                return 0 if isEven else -inf
            
            if dp[index][isEven] != -1:
                return dp[index][isEven]
            
            no_xor = nums[index] + maxSumOfNodes(index + 1, isEven)
            xor_done = (nums[index] ^ k) + maxSumOfNodes(index + 1, not isEven)

            dp[index][isEven] = max(no_xor, xor_done)
            return dp[index][isEven]
        
        return maxSumOfNodes(0, True)
