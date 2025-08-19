from imports import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_table = [0] * (n+1)
        for num in nums:
            hash_table[num] = 1
        
        result = []
        for num in range(1, n+1):
            if hash_table[num] == 0:
                result.append(num)
        
        return result
