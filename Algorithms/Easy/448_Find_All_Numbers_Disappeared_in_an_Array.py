from imports import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_table = [0] * (n + 1)
        for num in nums:
            hash_table[num] = 1
        
        ans = []
        for i in range(1, n+1):
            if hash_table[i] == 0:
                ans.append(i)
        
        return ans
