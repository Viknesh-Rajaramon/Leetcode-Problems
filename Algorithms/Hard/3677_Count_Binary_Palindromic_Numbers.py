class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        result = 1
        if n == 0:
            return result
        
        length = len(bin(n)) - 2
        for l in range(1, length):
            result += 1 << ((l - 1) // 2)
        
        low, p = 1 << ((length + 1) // 2 - 1), n >> (length // 2)
        if p > low:
            result += (p - low)
        
        x = p >> 1 if length % 2 else p
        for _ in range(length // 2):
            p = (p << 1) | (x & 1)
            x >>= 1

        if p <= n:
            result += 1
        
        return result
