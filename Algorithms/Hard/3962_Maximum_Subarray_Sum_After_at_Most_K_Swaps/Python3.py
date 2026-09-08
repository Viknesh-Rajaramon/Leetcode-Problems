from math import inf
from bisect import bisect_left, insort_left

class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        result, n, sorted_nums, initial_others, initial_candidates = -inf, len(nums), sorted(nums), [], []
        split = max(0, n-k)
        for i in range(split):
            initial_others.append(sorted_nums[i])

        for i in range(split, n):
            initial_candidates.append(sorted_nums[i])

        for start in range(n):
            candidates = initial_candidates.copy()
            others = initial_others.copy()
            current_sum = 0
            for end in range(start, n):
                if others:
                    pos = bisect_left(others, nums[end])
                    if pos < len(others) and others[pos] == nums[end]:
                        val = nums[end]
                        others.pop(pos)
                    else:
                        val = others.pop()

                    insort_left(candidates, val)

                current_sum += candidates.pop()
                result = max(result, current_sum)

        return result
