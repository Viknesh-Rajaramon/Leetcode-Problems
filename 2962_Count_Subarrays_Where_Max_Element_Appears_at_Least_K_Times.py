from imports import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)

        count = 0
        j = -1
        result = 0
        for i in range(n):
            while count < k and j + 1 < n:
                if nums[j+1] == max_element:
                    count += 1
            
                j += 1
            
            if count >= k:
                result += n-j
            
            if nums[i] == max_element:
                count -= 1
        
        return result
