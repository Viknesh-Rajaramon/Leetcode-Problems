from imports import *

class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        count = 0

        if n % 2 != 0:
            nums.append(0)
            count += 1
        
        i = 1
        while count < n:
            nums.append(i)
            nums.append(-i)
            count += 2
            i += 1
        
        return nums
