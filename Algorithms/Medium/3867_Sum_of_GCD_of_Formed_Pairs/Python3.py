from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        curr_max, prefix_gcd = 0, []
        for num in nums:
            curr_max = max(curr_max, num)
            prefix_gcd.append(gcd(num, curr_max))
        
        prefix_gcd.sort()
        result, left, right = 0, 0, len(nums)-1
        while left < right:
            result += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return result
