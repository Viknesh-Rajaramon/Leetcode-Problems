class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        upper = []
        while right:
            upper.append(right & 1)
            right >>= 1
        
        upper = upper[ : : -1]

        lower = []
        while left or len(lower) < len(upper):
            lower.append(left & 1)
            left >>= 1
        
        lower = lower[ : : -1]

        primes, dp = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}, {}
        def dfs(i: int, tight_low: bool, tight_high: bool, set_bits: int) -> int:
            if i == len(upper):
                return 1 if set_bits in primes else 0
            
            state = (i, tight_low, tight_high, set_bits)
            if state in dp:
                return dp[state]
            
            start = lower[i] if tight_low else 0
            end = upper[i] if tight_high else 1
            ways = 0
            for bit in range(start, end+1):
                ways += dfs(
                    i+1,
                    tight_low and bit == lower[i],
                    tight_high and bit == upper[i],
                    set_bits + (1 if bit == 1 else 0)
                )
            
            dp[state] = ways
            return ways

        return dfs(0, True, True, 0)
