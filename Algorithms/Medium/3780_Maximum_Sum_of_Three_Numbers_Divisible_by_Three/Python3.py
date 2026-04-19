from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        r_0, r_1, r_2 = [], [], []
        for num in nums:
            r = num % 3
            if r == 0:
                r_0.append(num)
            elif r == 1:
                r_1.append(num)
            else:
                r_2.append(num)
        
        r_0.sort(reverse = True)
        r_1.sort(reverse = True)
        r_2.sort(reverse = True)

        result = 0
        if len(r_0) >= 3:
            result = sum(r_0[ : 3])
        
        if len(r_1) >= 3:
            result = max(result, sum(r_1[ : 3]))
        
        if len(r_2) >= 3:
            result = max(result, sum(r_2[ : 3]))
        
        if len(r_0) >= 1 and len(r_1) >= 1 and len(r_2) >= 1:
            result = max(result, r_0[0] + r_1[0] + r_2[0])

        return result
