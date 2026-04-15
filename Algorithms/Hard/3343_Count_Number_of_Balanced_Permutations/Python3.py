mod = 10**9 + 7
max_n = 80

fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = (fact[i-1] * i) % mod

inv_fact = [1] * (max_n + 1)
inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
for i in range(max_n, 0, -1):
    inv_fact[i-1] = (inv_fact[i] * i) % mod

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        
        freq, total_sum = [0] * 10, 0

        for i in range(n):
            digit = ord(num[i]) - ord("0")
            freq[digit] += 1
            total_sum += digit
        
        if total_sum % 2:
            return 0
        
        even, odd, half_sum = (n+1)//2, n//2, total_sum//2

        dp = [[0] * (half_sum + 1) for _ in range(even + 1)]
        dp[0][0] = 1

        for digit in range(10):
            freq_digit = freq[digit]
            weight = [inv_fact[i] * inv_fact[freq_digit - i] for i in range(freq_digit+1)]
            w0 = weight[0]
            new_dp = [[(dp[k][s] * w0) % mod for s in range(half_sum + 1)] for k in range(even+1)]
            
            for j in range(1, freq_digit + 1):
                dk, ds, we = j, digit * j, weight[j]
                if dk > even or ds > half_sum:
                    break

                for k in range(even - dk, -1, -1):
                    row = dp[k]
                    tgt = new_dp[k + dk]
                    for s in range(half_sum - ds, -1, -1):
                        v = row[s]
                        if v:
                            tgt[s+ds] = (tgt[s+ds] + v * we) % mod
            
            dp = new_dp
        
        return (dp[even][half_sum] * fact[even] * fact[odd]) % mod
