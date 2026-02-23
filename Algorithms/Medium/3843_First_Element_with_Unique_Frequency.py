from typing import List
from collections import Counter

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        counts = Counter(nums)
        vals = Counter(counts.values())
        for num in nums:
            if vals[counts[num]] == 1:
                return num
        
        return -1
