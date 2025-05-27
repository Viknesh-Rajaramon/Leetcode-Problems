from imports import *

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        odd_count = 0
        curr_sum = 0

        for num in arr:
            curr_sum += num
            if curr_sum % 2:
                odd_count += 1
        
        return (odd_count * (n - odd_count + 1)) % (10**9 + 7)
