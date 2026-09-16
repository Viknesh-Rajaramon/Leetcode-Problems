class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 1000000007
    
        def modPow(base: int, exp: int) -> int:
            if exp == 0:
                return 1

            p = modPow(base, exp//2)
            p = (p * p) % mod
            if exp%2 == 0:
                return p

            return (p * (base % mod)) % mod

        def nCr(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0

            if r == 0 or r == n:
                return 1

            r = min(r, n-r)
            if n < mod and r < mod:
                num, den = 1, 1
                for i in range(1, r+1):
                    num = (num * (n+1-i)) % mod
                    den = (den * i) % mod

                return (num * modPow(den, mod-2)) % mod

            return (nCr(n // mod, r // mod) * nCr(n % mod, r % mod)) % mod

        return nCr(n+k-1, 2*k)
