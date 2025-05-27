class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        sign = -1 if num < 0 else 1
        base_7 = ""
        num = num * sign

        while num > 0:
            base_7 = base_7 + str(num % 7)
            num = num // 7
        
        return base_7[::-1] if sign == 1 else "-" + base_7[::-1]
