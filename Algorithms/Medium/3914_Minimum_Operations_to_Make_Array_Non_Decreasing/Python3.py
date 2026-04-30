from itertools import pairwise

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(a-b for a, b in pairwise(nums) if a > b)
