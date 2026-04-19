from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum_ = 0
        n = 0

        for i in range(len(nums)):
            if nums[i] % 6 == 0:
                sum_ += nums[i]
                n += 1

        if n == 0:
            return 0
            
        return int(sum_ / n)
