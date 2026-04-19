class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []

        while num > 0:
            digits.append(num % 10)
            num = num // 10
        
        digits.sort()

        min_sum = (digits[0] + digits[1])*10 + (digits[2] + digits[3])
        return min_sum
