class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse = True)
        result, end = 0, min(k, mul-1)
        for i in range(end):
            result += nums[i] * mul
            mul -= 1
        
        for i in range(end, k):
            result += nums[i]

        return result
