from imports import *

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score, curr_score = 0, 0
        s = set()
        left = 0
        for num in nums:
            if num in s:
                while nums[left] != num:
                    curr_score -= nums[left]
                    s.remove(nums[left])
                    left += 1
                
                left += 1
            else:
                s.add(num)
                curr_score += num
                if curr_score > max_score:
                    max_score = max(max_score, curr_score)
        
        return max_score
