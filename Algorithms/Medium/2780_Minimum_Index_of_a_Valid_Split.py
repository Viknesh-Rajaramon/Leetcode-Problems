from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        dominant_element = sorted(hash_map.items(), key=lambda x: x[1], reverse = True)[0]
        n = len(nums)

        count = 0
        for i in range(0, n-1):
            if nums[i] == dominant_element[0]:
                count += 1

                if count > (i+1)//2 and (dominant_element[1]-count) > (n-1-i)//2:
                    return i
        
        return -1
