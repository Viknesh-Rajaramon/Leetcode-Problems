class Solution:
    def findComplement(self, num: int) -> int:
        no_of_bits = 0
        x = num
        while x > 0:
            no_of_bits += 1
            x //= 2
        
        return pow(2, no_of_bits) - 1 - num
