from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i, num in zip(index, nums):
            if len(result) <= i:
                result.append(num)
            else:
                result.insert(i, num)
        
        return result
