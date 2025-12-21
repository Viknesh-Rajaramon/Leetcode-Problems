from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def count_valid_pairs(threshold: int) -> bool:
            i, count = 0, 0
            while i < n-1:
                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 1
                
                i += 1
            
            return count >= p
        
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2

            if count_valid_pairs(mid):
                high = mid
            else:
                low = mid + 1

        return low
