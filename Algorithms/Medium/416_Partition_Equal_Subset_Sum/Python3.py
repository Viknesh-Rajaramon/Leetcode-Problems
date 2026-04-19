from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total % 2:
            return False
        
        s = set([0, nums[0]])
        for i in range(1, len(nums)):
            temp = []
            for x in s:
                temp.append(x+nums[i])
            
            s.update(temp)
            if target in s:
                return True
        
        return False
