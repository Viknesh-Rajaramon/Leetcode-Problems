class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        mid = n//2
        result, half, total = 0, sum(nums[ : mid]), sum(nums)
        for i in range(n):
            if 2*half > total:
                result += 1

            half -= nums[i]
            half += nums[(mid+i)%n]

        return result
