class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        result, n, sum_, prod = -1, len(nums), sum(nums), 1
        for i in range(n-1, -1, -1):
            sum_ -= nums[i]
            if prod > sum_:
                break
            
            if sum_ == prod:
                result = i
            
            prod *= nums[i]

        return result
