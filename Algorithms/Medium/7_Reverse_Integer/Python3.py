class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        num = int(str(x)[ : : -1]) * sign
        if num < -2**31 or num >= 2**31:
            return 0
        
        return num
