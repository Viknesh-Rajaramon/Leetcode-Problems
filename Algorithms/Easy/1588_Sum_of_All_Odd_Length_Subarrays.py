from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        for i in range(n):
            result += arr[i] * (((n-i) * (i+1) + 1) // 2)
        
        return result
