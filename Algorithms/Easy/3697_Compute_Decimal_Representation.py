from imports import *

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result, place = [], 1
        while n > 0:
            digit = n % 10
            if digit != 0:
                result.append(digit * place)
            
            n //= 10
            place *= 10

        return result[::-1]
