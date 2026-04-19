class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        result, i, j = len(nums), -1, -1
        for k, num in enumerate(nums):
            if num == 1:
                i = k
                if j != -1:
                    result = min(result, abs(i-j))
            elif num == 2:
                j = k
                if i != -1:
                    result = min(result, abs(i-j))

        return result if result != len(nums) else -1
