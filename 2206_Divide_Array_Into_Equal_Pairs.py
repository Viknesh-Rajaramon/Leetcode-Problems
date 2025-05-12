from imports import *

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map = Counter(nums)
        
        for count in hash_map.values():
            if count % 2 == 1:
                return False
        
        return True
