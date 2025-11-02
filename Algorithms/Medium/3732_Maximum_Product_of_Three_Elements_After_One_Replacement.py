from imports import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return prod(nlargest(2, map(abs, nums))) * 10**5
