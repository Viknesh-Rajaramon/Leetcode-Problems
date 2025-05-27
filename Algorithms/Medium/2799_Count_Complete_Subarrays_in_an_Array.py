from imports import *

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        k = len(Counter(nums).keys())
        
        result = 0
        for l in range(n+1-k):
            s = set(nums[l: l+k])
            j = l+k
            while j < n and len(s) < k:
                s.add(nums[j])
                j += 1
            
            if len(s) == k:
                result += n+1-j

        return result
