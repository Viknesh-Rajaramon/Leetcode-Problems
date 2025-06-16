from imports import *

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        result = 0
        n = len(nums)
        
        left, right = Counter(nums[ : 1]), Counter(nums[1 : ])
        
        for j in range(1, n-1):
            right[nums[j]] -= 1
            
            curr = nums[j] * 2
            if left[curr] > 0 and right[curr] > 0:
                result = (result + (left[curr] * right[curr]) % mod) % mod
            
            left[nums[j]] += 1
            
        return result
