from imports import *

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n, mod = len(s)+1, 10**9 + 7
        prefix_count, prefix_sum, prefix_mod, pow_10 = [0] * n, [0] * n, [0] * n, [1] * n
        for i in range(1, n):
            pow_10[i] = pow_10[i-1] * 10 % mod
        
        for i in range(n-1):
            if s[i] != "0":
                prefix_count[i+1] = prefix_count[i] + 1
                prefix_sum[i+1] = prefix_sum[i] + int(s[i])
                prefix_mod[i+1] = (prefix_mod[i] * 10 + int(s[i])) % mod
            else:
                prefix_count[i+1] = prefix_count[i]
                prefix_sum[i+1] = prefix_sum[i]
                prefix_mod[i+1] = prefix_mod[i]

        result = []
        for l, r in queries:
            count = prefix_count[r+1] - prefix_count[l]
            sum_ = prefix_sum[r+1] - prefix_sum[l]

            if count == 0:
                result.append(0)
                continue
            
            num = (prefix_mod[r+1] - prefix_mod[l] * pow_10[count] % mod + mod) % mod
            result.append(num * sum_ % mod)

        return result
