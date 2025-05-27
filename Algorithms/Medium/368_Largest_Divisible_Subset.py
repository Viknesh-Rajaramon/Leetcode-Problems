from imports import *

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[nums[i]] for i in range(n)]
        length = [1] * n
        max_index = 0

        for i in reversed(range(n)):
            for j in range(i+1, n):
                if nums[j] % nums[i] != 0:
                    continue
                
                if length[j]+1 > length[i]:
                    dp[i] = [nums[i]] + dp[j]
                    length[i] = length[j]+1
            
            max_index = i if length[i] > length[max_index] else max_index

        return dp[max_index]
