MOD, MAX = 10**9+7, 10**5+1
fact = [1 for _ in range(MAX)]
for i in range(1, MAX):
    fact[i] = i * fact[i-1] % MOD

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        def bin_pow(x: int, y: int) -> int:
            result = 1
            while y:
                if y & 1:
                    result = result * x % MOD
                
                x = x * x % MOD
                y >>= 1

            return result % MOD
        
        return ((fact[n-1] * bin_pow(fact[n-1-k], MOD-2) * bin_pow(fact[k], MOD-2) % MOD)) * 2 % MOD
