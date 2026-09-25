class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        M = max(nums)
        spf = list(range(M+1))
        for i in range(2, int(M**0.5)+1):
            if spf[i] == i:
                for j in range(i*i, M+1, i):
                    if spf[j] == j:
                        spf[j] = i

        def prime_factors(x: int) -> set:
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p

            return factors

        result, l, freq = 0, 0, {}
        for r in range(len(nums)):
            for p in prime_factors(nums[r]):
                freq[p] = freq.get(p, 0) + 1

            while len(freq) > k:
                for p in prime_factors(nums[l]):
                    freq[p] -= 1
                    if freq[p] == 0:
                        del freq[p]

                l += 1

            result = max(result, r-l+1)
        
        return result
