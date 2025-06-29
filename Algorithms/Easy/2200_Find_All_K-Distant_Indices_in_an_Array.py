from imports import *

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        i = 0
        result = []
        for j in range(n):
            if nums[j] != key:
                continue
            
            i = max(i, j-k)
            while i < n and i <= j+k:
                result.append(i)
                i += 1

            if i == n:
                break
        
        return result
