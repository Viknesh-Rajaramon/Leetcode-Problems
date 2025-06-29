from imports import *

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = nums[ : : ]
        for n in nums:
            if n > 9:
                arr.append(int(str(n)[::-1]))
        
        return len(set(arr))
