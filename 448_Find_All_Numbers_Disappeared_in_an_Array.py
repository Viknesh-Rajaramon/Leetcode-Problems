from imports import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_table = [0] * (n)
        for i in range(n):
            hash_table[nums[i]-1] += 1
        
        ans = []
        for i in range(n):
            if hash_table[i] == 0:
                ans.append(i+1)
        
        return ans
