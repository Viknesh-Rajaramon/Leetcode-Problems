from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                for row in strs:
                    if row[i] < row[j]:
                        break
                else:
                    dp[i] = max(dp[i], 1+dp[j])

        return n - max(dp)
