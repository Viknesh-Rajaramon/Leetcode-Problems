from typing import List
from collections import Counter

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        
        groups = n // k
        for count in Counter(nums).values():
            if count > groups:
                return False
        
        return True
