from imports import *

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] < mn:
                mn = nums[i]
            
            if mx < nums[i]:
                mx = nums[i]
        
        gcd = 1
        for i in range(2, mn+1):
            if mn % i == 0 and mx % i == 0:
                gcd = i
        
        return gcd
