from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [num*num for num in nums]
        nums.sort(reverse = True)
        k = (len(nums)+1) // 2
        return sum(nums[ : k]) - sum(nums[k : ])
