from typing import List

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        nums.sort()
        sum_, result = [True] + [False] * k, [False] * n

        i = 0
        for x in range(1, n+1):
            while i < n and nums[i] < x:
                for j in range(k, nums[i] - 1, -1):
                    if sum_[j - nums[i]]:
                        sum_[j] = True
                
                i += 1
            
            for count in range(n-i+1):
                total_from_x = count * x
                if total_from_x > k:
                    break
                
                if sum_[k - total_from_x]:
                    result[x-1] = True
                    break
        
        return result
