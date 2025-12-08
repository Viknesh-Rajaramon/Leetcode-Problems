from imports import *

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        reverse = lambda x: int(bin(x)[-1 : 1 : -1], 2)
        nums.sort(key = lambda x: (reverse(x), x))
        return nums
