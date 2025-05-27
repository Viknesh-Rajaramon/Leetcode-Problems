class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def calculate(num: int) -> int:
            num = str(num)
            prefix_len = len(num) - len(s)

            if prefix_len < 0:
                return 0
            
            dp = [[0] * 2 for _ in range(prefix_len + 1)]

            dp[prefix_len][0] = 1
            dp[prefix_len][1] = int(num[prefix_len:]) >= int(s)
            
            for i in reversed(range(prefix_len)):
                digit = int(num[i])
                dp[i][0] = (limit + 1) * dp[i+1][0]
                if digit <= limit:
                    dp[i][1] = digit * dp[i+1][0] + dp[i+1][1]
                else:
                    dp[i][1] = dp[i][0]
            
            return dp[0][1]

        return calculate(finish) - calculate(start-1)
