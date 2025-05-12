from imports import *

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dp = [0] * (1000 + 1)

        n1 = len(nums1)
        for i in range(n1):
            dp[nums1[i]] += 1
        
        n2 = len(nums2)
        for i in range(n2):
            if dp[nums2[i]] > 0:
                ans.append(nums2[i])
                dp[nums2[i]] = 0
        
        return ans
