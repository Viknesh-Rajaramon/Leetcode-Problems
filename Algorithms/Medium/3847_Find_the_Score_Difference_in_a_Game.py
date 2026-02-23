from typing import List

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        result, active = 0, True
        for i, num in enumerate(nums):
            if i%6 == 5:
                active = not active
            
            if num%2:
                active = not active
            
            if active:
                result += num
            else:
                result -= num

        return result
