from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, ind_0 = len(nums), 0
        for i in range(n):
            if nums[i] == 0:
                ind_0 = i
                break
        
        for i in range(ind_0, ind_0+n-1):
            if nums[i%n] >= nums[(i+1)%n]:
                break
        else:
            return min(ind_0, n + 2 - ind_0)
        
        for i in range(ind_0, ind_0-n+1, -1):
            if nums[i%n] >= nums[(i-1)%n]:
                break
        else:
            return min(n - ind_0, 2 + ind_0)

        return -1
