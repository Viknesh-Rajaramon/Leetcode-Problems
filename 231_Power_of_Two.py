class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n <= 1:
                return True
            
            if n % 2 != 0:
                return False
            
            n = n // 2
        
        return False
