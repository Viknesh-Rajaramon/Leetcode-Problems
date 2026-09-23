class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n, target = len(nums), sum(nums) - x
        if target < 0:
            return -1
        
        result, l, curr_sum = -1, 0, 0
        for r in range(n):
            curr_sum += nums[r]
            while curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                result = max(result, r-l+1)

        return n - result if result != -1 else -1
