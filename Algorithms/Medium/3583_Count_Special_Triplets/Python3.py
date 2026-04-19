from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        result, mod, left, right = 0, 10**9+7, {}, {}
        for num in nums:
            if num % 2 == 0 and num//2 in right:
                result = (result + right[num//2]) % mod

            if num*2 in left:
                if num in right:
                    right[num] += left[num*2]
                else:
                    right[num] = left[num*2]
                
            if num in left:
                left[num] += 1
            else:
                left[num] = 1
            
        return result
