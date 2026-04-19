class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(0, n):
            xor = xor ^ (start + 2*i)
        
        return xor
