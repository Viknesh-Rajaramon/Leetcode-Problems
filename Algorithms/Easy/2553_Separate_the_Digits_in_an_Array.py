from imports import *

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def get_digits(num: int) -> List[int]:
            result = []
            while num > 0:
                result.append(num % 10)
                num //= 10
            
            return result[::-1]
        
        result = []
        for num in nums:
            result.extend(get_digits(num))
        
        return result
