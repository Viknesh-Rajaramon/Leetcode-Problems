class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        
        digits.sort()
        num1, num2 = 0, 0
        i, n = 0, len(digits)
        while i < n:
            num1 = num1*10 + digits[i]
            i += 1

            if i == n:
                break
            
            num2 = num2*10 + digits[i]
            i += 1
        
        return num1 + num2
