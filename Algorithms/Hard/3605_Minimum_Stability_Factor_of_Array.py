from imports import *

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)

        def helper(max_len: int) -> bool:
            i, count = 0, 0
            while i <= n - max_len:
                hcf = nums[i]
                for j in range(1, max_len):
                    hcf = gcd(hcf, nums[i+j])
                    if hcf == 1:
                        break
                    
                if hcf >= 2:
                    count += 1
                    if count > maxC:
                        return False
                    
                    i += max_len
                else:
                    i += 1

            return True
        
        result = 0

        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2

            if helper(mid):
                high = mid - 1
            else:
                result = mid
                low = mid + 1
        
        return result
