from typing import List
from math import inf
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        result = inf
        k -= 2
        cost = nums.pop(0)
        window = SortedList(nums[ : dist])
        cost += sum(window[ : k])
        for left, right in zip(nums, nums[dist : ]):
            window.add(right)
            cost += min(window[k], right)
            result = min(result, cost)
            cost -= min(window[k], left)
            window.remove(left)

        return result
