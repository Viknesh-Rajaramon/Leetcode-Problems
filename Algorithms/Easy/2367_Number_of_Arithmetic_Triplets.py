from imports import *

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        result = 0
        for num in s:
            if num+diff in s and num+2*diff in s:
                result += 1
        
        return result
