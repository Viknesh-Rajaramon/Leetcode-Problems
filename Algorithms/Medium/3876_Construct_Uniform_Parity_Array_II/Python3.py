from math import inf

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd, min_even = inf, inf
        for num in nums1:
            if num%2:
                min_odd = min(min_odd, num)
            else:
                min_even = min(min_even, num)
        
        if min_odd == inf or min_even == inf:
            return True
        
        return min_even > min_odd
