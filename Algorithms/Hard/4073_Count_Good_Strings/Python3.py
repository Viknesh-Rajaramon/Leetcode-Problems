class Solution:
    def countGoodStrings(self, n: int) -> int:
        mod = 10**9+7
        def fib(k: int) -> list[int]:
            if k == 0:
                return [0, 1]

            f = fib(k >> 1)
            c = f[0] * ((2*f[1] - f[0] + mod) % mod) % mod
            d = ((f[0] * f[0] % mod) + (f[1] * f[1] % mod)) % mod
            if k & 1:
                return [d, (c+d) % mod]
            
            return [c, d]
        
        return (2 * fib(n)[0]) % mod
