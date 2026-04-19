from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        dup_ptr = 1
        count = False if nums[0] != nums[1] else True
        k = 2

        for i in range(2, len(nums)):
            if nums[dup_ptr] != nums[i]:
                dup_ptr += 1
                nums[dup_ptr] = nums[i]
                k += 1
                count = False
            else:
                if not count:
                    count = True
                    dup_ptr += 1
                    nums[dup_ptr] = nums[i]
                    k += 1
        
        return k
