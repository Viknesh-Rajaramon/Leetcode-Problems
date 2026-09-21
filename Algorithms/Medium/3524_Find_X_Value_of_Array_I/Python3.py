from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result, dp = [0] * k, [0] * k
        for num in nums:
            new_dp = [0] * k
            new_dp[num % k] += 1
            for r in range(k):
                new_dp[(r*num) % k] += dp[r]

            dp = new_dp
            for r in range(k):
                result[r] += dp[r]

        return result
