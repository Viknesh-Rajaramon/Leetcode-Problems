from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        pos = defaultdict(list)
        for i, p in enumerate(prefix_sum):
            pos[p].append(i)
        
        result, last = 0, {}
        for i, num in enumerate(nums):
            low, high = last.get(num, -1)+1, i
            last[num] = i

            left, right = high-low+1, n-i
            if left < right:
                for j in range(low, high+1):
                    target = prefix_sum[j] + num
                    if target in pos:
                        result += len(pos[target]) - bisect_left(pos[target], i+1)
            else:
                for j in range(i+1, n+1):
                    target = prefix_sum[j] - num
                    if target in pos:
                        result += bisect_right(pos[target], high) - bisect_left(pos[target], low)

        return result
