from typing import List
from math import inf

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        result, i = 0, 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                best, idx = inf, 0
                for j in range(len(nums)-1):
                    s = nums[j] + nums[j+1]
                    if s < best:
                        best, idx = s, j

                nums[idx : idx+2] = [best]
                result += 1
                i = 0
            else:
                i += 1
        
        return result
