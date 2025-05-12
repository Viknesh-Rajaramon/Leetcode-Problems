class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = []
        for i in range(len(s)):
            digits.append(int(s[i]))

        while len(digits) > 2:
            new = []
            for i in range(1, len(digits)):
                new.append((digits[i-1] + digits[i]) % 10)

            digits = new

        if digits[0] == digits[1]:
            return True
        
        return False
