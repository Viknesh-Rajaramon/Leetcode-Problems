class Solution:
    def reverseBits(self, n: int) -> int:
        power, result = 31, 0
        while n > 0:
            if n % 2:
                result += 2**power
            
            n //=  2
            power -= 1
        
        return result
