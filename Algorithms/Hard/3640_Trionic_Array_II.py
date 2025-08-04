from imports import *

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        result = -inf
        
        incs, decs, incl, incr = -inf, -inf, -inf, False
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                if incr:
                    incs = max(incs, nums[i]) + nums[i + 1]
                    incl += nums[i + 1]
                else:
                    incs = nums[i + 1] + nums[i]
                    incl = decs + nums[i + 1]
                
                incr = True
            elif nums[i + 1] < nums[i]:
                if incr:
                    decs = incs + nums[i + 1]
                else:
                    decs += nums[i + 1]
                
                incr = False
            else:
                incs, decs, incl, incr = -inf, -inf, -inf, False
            
            result = max(result, incl)

        return result
