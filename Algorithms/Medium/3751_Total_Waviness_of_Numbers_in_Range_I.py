class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0
        for num in range(num1, num2+1):
            x, s = 0, str(num)
            for j in range(1, len(s)-1):
                if s[j] < s[j-1] and s[j] < s[j+1]:
                    x += 1
                
                if s[j] > s[j-1] and s[j] > s[j+1]:
                    x += 1

            result += x

        return result
