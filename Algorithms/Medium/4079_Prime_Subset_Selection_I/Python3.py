class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n == 1 or s == 1:
            return []

        is_prime = [True] * (n+1)
        is_prime[0], is_prime[1], i = False, False, 2
        while i*i <= n:
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False

            i += 1

        result, total = [], 0
        for prime in range(2, n+1):
            if is_prime[prime]:
                if total + prime > s:
                    break

                total += prime
                result.append(prime)
        
        return result
