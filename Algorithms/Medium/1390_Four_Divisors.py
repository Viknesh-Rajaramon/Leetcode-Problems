from typing import List
from collections import Counter
from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def sum_4_divisors(num: int) -> List[int]:
            divisors = set()
            
            i = 1
            while i <= sqrt(num):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                    if len(divisors) > 4:
                        return 0
                
                i += 1
            
            if len(divisors) == 4:
                return sum(divisors)
            
            return 0
        
        counts = Counter(nums)
        result = 0
        for num, count in counts.items():
            result += sum_4_divisors(num) * count
        
        return result
