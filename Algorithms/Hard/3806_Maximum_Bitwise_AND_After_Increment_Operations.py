from typing import List

class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        nums.sort()
        n, x, remain = len(nums), 0, nums[-1]
        while remain > 0:
            x += 1
            remain = remain >> 1
        
        result, start = 0, 1 << x
        while k > 0:
            val = sum(start-nums[i] for i in range(n-1, n-m-1, -1))
            if k < val:
                break
            
            result = start
            for i in range(n-1, n-m-1, -1):
                nums[i] = start
                
            k -= val
            start = start << 1
        
        start = start >> 1
        while k > 0 and start > 0:
            if start == result:
                start = start >> 1
                continue
            
            val = 0
            for i in range(n-1, n-m-1, -1):
                diff = result + start - nums[i]
                if diff > 0:
                    val += diff
                    
            if k >= val:
                result += start
                k -= val
                for i in range(n-1, n-m-1, -1):
                    if result > nums[i]:
                        nums[i] = result
            else:
                for i in range(n-1, -1, -1):
                    nums[i] = nums[i] & (~start)
                
                nums.sort()
                
            start = start >> 1

        return result
