from imports import *

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr: List[int]) -> bool:
            min_ = min(arr)
            max_ = max(arr)

            if (max_ - min_) % (len(arr) - 1) != 0:
                return False
            
            diff = (max_ - min_) // (len(arr) - 1)
            
            arr = set(arr)
            curr = min_ + diff
            while curr < max_:
                if curr not in arr:
                    return False
                
                curr += diff
            
            return True

        return [check(nums[i : j+1]) for i, j in zip(l, r)]
