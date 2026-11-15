from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n, odd_count, curr_sum = len(arr), 0, 0
        for num in arr:
            curr_sum += num
            if curr_sum % 2:
                odd_count += 1
        
        return (odd_count * (n - odd_count + 1)) % (10**9 + 7)
