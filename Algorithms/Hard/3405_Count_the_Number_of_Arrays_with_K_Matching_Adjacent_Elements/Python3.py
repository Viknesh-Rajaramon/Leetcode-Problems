MOD = 10**9 + 7
M = 10**5 + 1

fact = [1] * M
inv_fact = [1] * M

for i in range(1, M):
    fact[i] = (fact[i-1] * i) % MOD
    inv_fact[i] = pow(fact[i], MOD - 2, MOD)

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        def nCr(n: int, r: int) -> int:
            return fact[n] * inv_fact[r] * inv_fact[n-r] % MOD

        return m * nCr(n-1, k) * pow(m-1, n-k-1, MOD) % MOD
