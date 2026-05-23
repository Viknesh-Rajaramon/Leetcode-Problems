from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 1 if nums[0] < nums[-1] else 0
        count += sum(1 for i in range(len(nums)-1) if nums[i] > nums[i+1])
        return count <= 1
