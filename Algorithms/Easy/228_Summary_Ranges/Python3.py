from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        count = 1
        start = nums[0]
        result = []
        
        for i in range(1, len(nums)):
            if nums[i] == start + count:
                count += 1
            else:
                temp = [str(start)]
                if count > 1:
                    temp.append("->")
                    temp.append(str(start + count - 1))

                result.append("".join(temp))
                start = nums[i]
                count = 1
        
        temp = [str(start)]
        if count > 1:
            temp.append("->")
            temp.append(str(start + count - 1))

        result.append("".join(temp))
        return result
