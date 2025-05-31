from imports import *

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i in range(len(num2)):
            carry = 0
            result *= 10
            temp = deque()
            for j in range(len(num1)-1, -1, -1):
                digit = int(num1[j]) * int(num2[i]) + carry
                carry = digit // 10
                temp.appendleft(digit % 10)
            
            if carry > 0:
                temp.appendleft(carry)

            num = 0
            for c in temp:
                num = num*10 + c

            result += num

        return str(result)
