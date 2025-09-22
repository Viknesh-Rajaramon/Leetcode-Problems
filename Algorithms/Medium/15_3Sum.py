from imports import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
