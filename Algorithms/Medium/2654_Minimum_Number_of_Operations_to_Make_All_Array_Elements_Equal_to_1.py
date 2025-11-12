from imports import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, ones = len(nums), nums.count(1)
        if ones:
            return n - ones
        
        result = inf
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    result = min(result, j-i)

        return result + n - 1 if result != inf else -1
