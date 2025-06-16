from imports import *

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            
            s.add(n)
        
        return 0
