from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def is_bin_palindrome(n: int) -> bool:
            s = bin(n)[2 : ]
            return s == s[::-1]
        
        result = []
        for num in nums:
            ops = 0
            if not is_bin_palindrome(num):
                while True:
                    ops += 1
                    if is_bin_palindrome(num-ops) or is_bin_palindrome(num+ops):
                        break


            result.append(ops)

        return result
