from imports import *

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        result, prefix_sum, k_sum = -inf, 0, [inf] * (k-1) + [0]
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = i%k
            sub_sum = prefix_sum - k_sum[mod]

            if sub_sum > result:
                result = sub_sum
            
            if prefix_sum < k_sum[mod]:
                k_sum[mod] = prefix_sum

        return result
