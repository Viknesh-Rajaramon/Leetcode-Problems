from math import inf

class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        mod, n, max_val = 10**9+7, len(nums), 0
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            max_val = max(max_val, nums[i])

        if prefix[n] == n:
            return mod-2

        spf, i = [i for i in range(max_val+1)], 2
        while i*i <= max_val:
            if spf[i] == i:
                for j in range(i*i, max_val+1, i):
                    if spf[j] == j:
                        spf[j] = i

            i += 1
        
        mix, max_diff, best_k = [0] * (max_val+1), -inf, 0
        for i, num in enumerate(nums):
            x = num
            while x > 1:
                p = spf[x]
                diff = max(0, mix[p] - prefix[i]) + num
                if diff > max_diff or (diff == max_diff and p < best_k):
                    max_diff, best_k = diff, p

                mix[p] = diff + prefix[i+1]
                while x%p == 0:
                    x //= p

        return max_diff * best_k % mod
