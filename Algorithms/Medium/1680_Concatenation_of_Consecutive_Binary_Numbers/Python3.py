class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result, mod = 0, 10**9+7
        for i in range(1, n+1):
            result = (result << i.bit_length()) % mod + i

        return result % mod
