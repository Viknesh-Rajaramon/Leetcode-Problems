from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]

        for i, val in enumerate(stoneValue):
            left[i][i], right[i][i] = val, val

        for start in range(n-2, -1, -1):
            total_sum, split_at, left_sum = stoneValue[start], start, 0
            for end in range(start+1, n):
                total_sum += stoneValue[end]
                while split_at <= end and 2 * (left_sum + stoneValue[split_at]) <= total_sum:
                    left_sum += stoneValue[split_at]
                    split_at += 1
                
                if left_sum * 2 == total_sum:
                    dp[start][end] = max(left[start][split_at-1], right[split_at][end])
                else:
                    if start == split_at:
                        dp[start][end] = right[split_at+1][end] if split_at+1 <= end else 0
                    else:
                        dp[start][end] = max(
                            left[start][split_at-1] if split_at-1 >= start else 0,
                            right[split_at+1][end] if split_at+1 <= end else 0
                        )
                
                left[start][end] = max(left[start][end-1], total_sum + dp[start][end])
                right[start][end] = max(right[start+1][end], total_sum + dp[start][end])
        
        return dp[0][-1]
