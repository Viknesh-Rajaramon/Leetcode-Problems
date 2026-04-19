class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if num < 10:
                break
            
            sum_ = 0
            while num > 0:
                sum_ += num % 10
                num = num // 10
            num = sum_
        
        return num
