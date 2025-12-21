from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_ = max(nums)
        count = [0] * (max_+1)
        for num in nums:
            count[num] += 1
        
        left, right, result = 0, sum(count[ : k]), 0
        for num in range(max_+1):
            right -= count[num]
            if num+k <= max_:
                right += count[num+k]
            if num > 0:
                left += count[num-1]
            if num > k+1:
                left -= count[num-k-1]
            
            result = max(result, count[num] + min(left + right, numOperations))
        
        return result
