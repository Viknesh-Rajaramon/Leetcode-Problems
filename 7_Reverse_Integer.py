class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)
        if x >= 0:
            new = int(n[::-1])
            return new if new <= 2**31 - 1 else 0
        
        new = int(n[0] + n[:0:-1])
        
        return new if new >= -2**31 else 0
