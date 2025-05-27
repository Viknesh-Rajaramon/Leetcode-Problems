class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        for i in range(1, len(s)):
            if romanToIntMap[s[i-1]] < romanToIntMap[s[i]]:
                num -= romanToIntMap[s[i-1]]
            else:
                num += romanToIntMap[s[i-1]]
        
        num += romanToIntMap[s[-1]]
        return num
