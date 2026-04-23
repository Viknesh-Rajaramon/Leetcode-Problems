from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n, groups = len(nums), defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)
        
        result = [0] * n
        for indices in groups.values():
            total, prefix_sum, size = sum(indices), 0, len(indices)
            for j, idx in enumerate(indices):
                result[idx] = total - 2*prefix_sum + idx*(2*j - size)
                prefix_sum += idx

        return result
