from imports import *

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return n

        nums.sort()
        result, threshold = 0, nums[n-k]
        for num in nums:
            if num < threshold:
                result += 1

        return result
