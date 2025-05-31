from imports import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        result = []
        i = 0
        while i < n-3:
            j = i + 1
            while j < n-2:
                left, right = j + 1, n-1

                remaining_sum = target - nums[i] - nums[j]
                while left < right:
                    curr_sum = remaining_sum - nums[left] - nums[right]

                    if curr_sum == 0:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left + 1 < n and nums[left] == nums[left+1]:
                            left += 1
                        
                        left += 1
                        right -= 1
                    elif curr_sum > 0:
                        left += 1
                    else:
                        right -= 1
                
                while j + 1 < n and nums[j] == nums[j+1]:
                    j += 1

                j += 1

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            
            i += 1

        return result
