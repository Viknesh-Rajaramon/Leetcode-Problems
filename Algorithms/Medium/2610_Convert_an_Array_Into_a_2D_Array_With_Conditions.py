from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        max_count = max(counts.values())
        
        result = [[] for _ in range(max_count)]
        for num, count in counts.items():
            for j in range(count):
                result[j].append(num)
        
        return result
