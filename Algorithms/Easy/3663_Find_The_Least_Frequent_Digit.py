from collections import Counter
from math import inf

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        digits = list(map(int, str(n)))
        freq = Counter(digits)
        
        min_digit, min_count = inf, inf
        for digit, count in freq.items():
            if count < min_count:
                min_count = count
                min_digit = digit
            elif count == min_count and digit < min_digit:
                min_digit = digit
        
        return min_digit
