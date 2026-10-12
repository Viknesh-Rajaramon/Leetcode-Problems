from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod, count = 10**9+7, [0] * 30
        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    count[i] += 1
        
        result = 0
        for _ in range(k):
            curr = 0
            for j in range(29, -1, -1):
                if count[j] == 0:
                    continue
                
                curr |= 1 << j
                count[j] -= 1
            
            result = (result + curr * curr) % mod

        return result
