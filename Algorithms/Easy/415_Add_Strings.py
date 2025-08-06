class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        n1, n2 = len(num1), len(num2)
        n = max(n1, n2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        num = ""

        i = 0
        while i < n1 and i < n2:
            x = int(num1[i]) + int(num2[i]) + carry
            carry = int(x / 10)
            num = num + str(x % 10)
            i += 1
        
        while i < n1:
            x = int(num1[i]) + carry
            carry = int(x / 10)
            num = num + str(x % 10)
            i += 1
        
        while i < n2:
            x = int(num2[i]) + carry
            carry = int(x / 10)
            num = num + str(x % 10)
            i += 1
        
        if carry > 0:
            num = num + str(carry)
        
        return num[ : : -1]
