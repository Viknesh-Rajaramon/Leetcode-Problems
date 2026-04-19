from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        
        result = [1] * n
        for i in range(n):
            j = i - 1
            while j >= 0 and nums[j] | nums[i] != nums[j]:
                result[j] = i - j + 1
                nums[j] |= nums[i]
                j -= 1

        return result
