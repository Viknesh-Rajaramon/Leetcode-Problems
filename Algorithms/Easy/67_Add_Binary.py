class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""

        a = a[::-1]
        b = b[::-1]

        i = 0
        carry = 0
        while i < len(a) and i < len(b):
            if a[i] == "0" and b[i] == "0" and carry == 0:
                res += "0"
                carry = 0
            elif a[i] == "0" and b[i] == "0" and carry == 1:
                res += "1"
                carry = 0
            elif a[i] == "0" and b[i] == "1" and carry == 0:
                res += "1"
                carry = 0
            elif a[i] == "0" and b[i] == "1" and carry == 1:
                res += "0"
                carry = 1
            elif a[i] == "1" and b[i] == "0" and carry == 0:
                res += "1"
                carry = 0
            elif a[i] == "1" and b[i] == "0" and carry == 1:
                res += "0"
                carry = 1
            elif a[i] == "1" and b[i] == "1" and carry == 0:
                res += "0"
                carry = 1
            elif a[i] == "1" and b[i] == "1" and carry == 1:
                res += "1"
                carry = 1
            
            i += 1
        
        while i < len(a):
            if a[i] == "0" and carry == 0:
                res += "0"
                carry = 0
            elif a[i] == "0" and carry == 1:
                res += "1"
                carry = 0
            elif a[i] == "1" and carry == 0:
                res += "1"
                carry = 0
            elif a[i] == "1" and carry == 1:
                res += "0"
                carry = 1
            
            i += 1
        
        while i < len(b):
            if b[i] == "0" and carry == 0:
                res += "0"
                carry = 0
            elif b[i] == "0" and carry == 1:
                res += "1"
                carry = 0
            elif b[i] == "1" and carry == 0:
                res += "1"
                carry = 0
            elif b[i] == "1" and carry == 1:
                res += "0"
                carry = 1
            
            i += 1
        
        if carry == 1:
            res += "1"
        
        res = res[::-1]
        return res
