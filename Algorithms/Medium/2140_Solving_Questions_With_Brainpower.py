from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            temp = dp[i+1 + questions[i][1]] if i+1+questions[i][1] <= n else 0
            dp[i] = max(dp[i+1], questions[i][0] + temp)
        
        return dp[0]
