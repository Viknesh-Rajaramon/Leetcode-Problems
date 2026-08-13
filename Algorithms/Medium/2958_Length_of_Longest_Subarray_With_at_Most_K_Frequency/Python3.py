from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result, l, freq = 0, 0, {}
        for r, num in enumerate(nums):
            freq[num] = freq.get(num, 0)+1
            while freq[num] > k:
                freq[nums[l]] -= 1
                l += 1

            result = max(result, r-l+1)
        
        return result
