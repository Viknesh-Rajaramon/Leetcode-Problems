from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9+7
        def dfs(nums: list[int]) -> int:
            n = len(nums)
            if n <= 2:
                return 1
            
            left, right = [], []
            for num in nums[1 : ]:
                if num < nums[0]:
                    left.append(num)
                else:
                    right.append(num)

            return dfs(left) * dfs(right) * comb(n-1, len(left))

        return (dfs(nums) - 1) % mod
