from imports import *

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        result = 0
        for key in counts.keys():
            if key+1 in counts:
                result = max(result, counts[key] + counts[key+1])
            
        return result
