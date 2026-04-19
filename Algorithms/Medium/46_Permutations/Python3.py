from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        def permute(i: int):
            if i == n:
                result.append(nums.copy())
                return
            
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                permute(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        permute(0)
        return result
