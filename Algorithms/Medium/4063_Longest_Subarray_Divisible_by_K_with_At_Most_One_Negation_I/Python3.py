class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        result, n = 0, len(nums)
        for l in range(n):
            curr_sum, seen = 0, set()
            for r in range(l, n):
                curr_sum += nums[r]
                seen.add((2*nums[r])%k)
                target = curr_sum%k
                if target == 0 or target in seen:
                    result = max(result, r-l+1)

        return result
