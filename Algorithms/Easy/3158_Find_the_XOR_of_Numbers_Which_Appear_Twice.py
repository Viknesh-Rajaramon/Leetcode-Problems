from imports import *

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor = 0
        s = set()
        for num in nums:
            if num in s:
                xor ^= num
            else:
                s.add(num)
        
        return xor
