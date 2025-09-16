from imports import *

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result = []

        curr = nums[0]
        for num in nums[1 : ]:
            if gcd(curr, num) > 1:
                curr = lcm(curr, num)

                while result and gcd(curr, result[-1]) > 1:
                    curr = lcm(curr, result.pop())
            else:
                result.append(curr)
                curr = num
                
        result.append(curr)

        return result
