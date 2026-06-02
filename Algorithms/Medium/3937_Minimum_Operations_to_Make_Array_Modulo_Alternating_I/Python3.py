from math import inf

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] %= k

        cost_odd, cost_even = [0] * k, [0] * k
        for i, num in enumerate(nums):
            for target in range(k):
                d = (num - target) % k
                c = d if d <= k-d else k-d
                if i%2:
                    cost_odd[target] += c
                else:
                    cost_even[target] += c

        result = inf
        for x in range(k):
            for y in range(k):
                if x == y:
                    continue

                result = min(result, cost_even[x]+cost_odd[y])
        
        return result
