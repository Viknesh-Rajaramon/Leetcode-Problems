class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum, num = 0, x
        while num > 0:
            digit_sum += num % 10
            num //= 10
        
        return digit_sum if x % digit_sum == 0 else -1
