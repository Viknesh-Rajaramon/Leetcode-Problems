class Solution:
    def isPowerOfThree(self, n: int) -> bool:        
        new_num = 1
        while new_num <= n:
            if new_num == n:
                return True
            
            new_num *= 3
        
        return False
