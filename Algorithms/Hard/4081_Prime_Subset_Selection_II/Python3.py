from math import inf

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        if n == 1 or s == 1:
            return []

        is_prime = [True] * (n+1)
        is_prime[0], is_prime[1], i = False, False, 2
        while i*i <= n:
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False

            i += 1

        primes = [prime for prime in range(2, n+1) if is_prime[prime]]
        n = len(primes)
        dp = [[inf] * (s+1) for _ in range(n+1)]
        dp[n][0] = 0
        for i in range(n-1, -1, -1):
            for t in range(s+1):
                best = dp[i+1][t]
                if t >= primes[i] and dp[i+1][t - primes[i]] != inf and dp[i+1][t - primes[i]]+1 < best:
                    best = dp[i+1][t - primes[i]]+1

                dp[i][t] = best

        target = 0
        for t in range(s, 0, -1):
            if dp[0][t] != inf:
                target = t
                break

        if target == 0:
            return []

        result, need = [], dp[0][target]
        for i in range(n):
            if need == 0:
                break

            if primes[i] <= target and dp[i+1][target - primes[i]] == need-1:
                result.append(primes[i])
                target -= primes[i]
                need -= 1
            
        return result
