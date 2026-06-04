class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0
        for num in range(num1, num2+1):
            s = str(num)
            for j in range(1, len(s)-1):
                if s[j-1] > s[j] < s[j+1] or s[j-1] < s[j] > s[j+1]:
                    result += 1

        return result
