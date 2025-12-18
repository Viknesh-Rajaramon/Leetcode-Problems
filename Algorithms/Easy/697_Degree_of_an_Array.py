from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        indexes = defaultdict(list)

        n = len(nums)
        for i in range(n):
            counts[nums[i]] += 1
            indexes[nums[i]].append(i)
        
        max_count, min_length = 0, 0
        for num, count in counts.items():
            if max_count < count:
                max_count = count
                min_length = indexes[num][-1] - indexes[num][0]
            elif max_count == count and indexes[num][-1] - indexes[num][0] < min_length:
                min_length = indexes[num][-1] - indexes[num][0]
        
        return min_length + 1
