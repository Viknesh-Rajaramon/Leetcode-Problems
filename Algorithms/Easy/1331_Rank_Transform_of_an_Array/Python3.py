from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks, nums = {}, sorted(set(arr))
        for i, num in enumerate(nums, 1):
            ranks[num] = i

        return [ranks[num] for num in arr]
