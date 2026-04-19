class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * n for n in range(1, 102)]
        dp[0][0] = poured
        for row in range(query_row+1):
            for col in range(row+1):
                q = (dp[row][col] - 1)/2
                if q > 0:
                    dp[row+1][col] += q
                    dp[row+1][col+1] += q

        return min(1, dp[query_row][query_glass])
