from typing import List
from collections import Counter

class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        bad = [i for i in range(n) if nums[i] == forbidden[i]]
        k = len(bad)

        if k == 0:
            return 0

        count_nums, count_forbidden = Counter(nums), Counter(forbidden)
        for num in count_nums:
            if count_nums[num] + count_forbidden[num] > n:
                return -1
    
        return max(max(Counter(forbidden[i] for i in bad).values()), (k+1) // 2)
