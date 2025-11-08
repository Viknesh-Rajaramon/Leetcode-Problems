class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result, k, mask = 0, 0, 1
        while mask <= n:
            if n & mask:
                result = 2 ** (k+1) - 1 - result
            
            mask <<= 1
            k += 1

        return result
