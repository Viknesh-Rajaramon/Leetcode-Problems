from imports import *

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            if not len(str(n)) % 2:
                result += 1
        
        return result
