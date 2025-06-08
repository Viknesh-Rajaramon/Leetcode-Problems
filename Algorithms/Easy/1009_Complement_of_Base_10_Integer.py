class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        no_of_bits = 0
        x = n
        while x > 0:
            no_of_bits += 1
            x //= 2
        
        return pow(2, no_of_bits) - 1 - n
