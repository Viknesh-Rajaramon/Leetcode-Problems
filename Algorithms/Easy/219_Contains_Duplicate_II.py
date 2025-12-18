from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num not in num_index:
                num_index[num] = i
                continue
            
            if abs(i - num_index[num]) <= k:
                return True
            
            num_index[num] = i
        
        return False
