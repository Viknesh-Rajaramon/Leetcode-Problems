from imports import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest_sum = nums[0] + nums[1] + nums[2]
        if closest_sum >= target:
            return closest_sum

        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == target:
                    return target
                
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
