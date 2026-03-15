from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n, curr_max, prefix_gcd = len(nums), 0, []
        for num in nums:
            curr_max = max(curr_max, num)
            prefix_gcd.append(gcd(num, curr_max))
        
        prefix_gcd.sort()
        return sum(gcd(prefix_gcd[i], prefix_gcd[n-1-i]) for i in range(n//2))
