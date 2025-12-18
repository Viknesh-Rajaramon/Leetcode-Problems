from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            new = digits[i] + carry
            digits[i] = new % 10
            carry = new // 10
        
        return [1] + digits if carry == 1 else digits
