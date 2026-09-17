from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        result, n, total = len(arr)+1, len(arr), 0
        dp, l = [n] * (n+1), 0
        for r, num in enumerate(arr):
            total += num
            while total > target:
                total -= arr[l]
                l += 1
            
            dp[r+1] = dp[r]
            if total == target:
                result = min(result, r-l+1+dp[l])
                dp[r+1] = min(dp[r], r-l+1)

        return result if result != n+1 else -1
