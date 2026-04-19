from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        def generate_subset(i: int, subset: List[int]) -> None:
            if i == len(nums):
                result.append(subset)
                return
            
            generate_subset(i+1, subset + [nums[i]])

            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            
            generate_subset(i+1, subset)

        generate_subset(0, [])
        return result
