from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num == target:
                result.append(i)
            elif num > target:
                break
        
        return result
