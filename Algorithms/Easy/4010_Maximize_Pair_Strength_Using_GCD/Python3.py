from math import gcd

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        result, n = 0, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                g = gcd(nums[i], nums[j])
                result = max(result, (nums[i] * nums[j]) // (g*g))

        return result
