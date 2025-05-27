from imports import *

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(num: int) -> int:
            sum_ = 0
            while num > 0:
                sum_ += num % 10
                num //= 10

            return sum_
        
        count = defaultdict(int)
        for i in range(1, n+1):
            count[sum_digits(i)] += 1
        
        max_val = 0
        result = 0
        for c in count.values():
            if c > max_val:
                result = 1
                max_val = c
            elif c == max_val:
                result += 1
        
        return result
