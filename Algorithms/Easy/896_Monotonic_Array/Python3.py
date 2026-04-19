from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        def checkMonotonic(nums: List[int]) -> bool:
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    return False
            
            return True

        return checkMonotonic(nums) or checkMonotonic(nums[::-1])
