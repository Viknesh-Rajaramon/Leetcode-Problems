from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def generate_subset(i: int, subset: List[int]) -> None:
            if i == len(nums):
                result.append(subset)
                return
            
            generate_subset(i+1, subset)
            generate_subset(i+1, subset + [nums[i]])

        generate_subset(0, [])
        return result
