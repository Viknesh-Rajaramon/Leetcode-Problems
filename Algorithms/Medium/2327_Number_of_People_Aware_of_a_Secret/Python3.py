class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp, ppl = [1] + [0] * (n - 1), 0
        for today in range(delay, n):
            ppl += dp[today-delay]
            dp[today] += ppl
            if today - forget + 1 >= 0:
                ppl -= dp[today - forget + 1]

        return sum(dp[-forget : : ]) % (10**9 + 7)
