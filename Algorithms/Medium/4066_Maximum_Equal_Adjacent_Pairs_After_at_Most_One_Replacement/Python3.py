from collections import defaultdict

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        result, n, base, count = 0, len(nums), 0, defaultdict(int)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                base += 1
            else:
                p = (min(nums[i], nums[i+1]), max(nums[i], nums[i+1]))
                count[p] += 1
                result = max(result, count[p])

        return base + result
