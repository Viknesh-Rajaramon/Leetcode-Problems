from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def combinations(i: int, nums: List[int]):
            if len(nums) == k:
                result.append(nums.copy())
                return
            
            for j in range(i+1, n+1):
                nums.append(j)
                combinations(j, nums)
                nums.pop()
        
        combinations(0, [])
        return result
