from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        for val, c in sorted(Counter(nums).items(), key = lambda x: (x[1], -x[0])):
            result.extend([val] * c)
        
        return result
