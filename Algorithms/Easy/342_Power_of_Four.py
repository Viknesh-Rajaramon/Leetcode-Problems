from imports import *

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return int(log2(n) / 2) == (log2(n) / 2)
