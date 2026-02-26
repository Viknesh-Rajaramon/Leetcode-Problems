class Solution:
    def numSteps(self, s: str) -> int:
        result, num = 0, int(s, 2)
        while num > 1:
            if num % 2:
                num += 1
            else:
                num >>= 1
            
            result += 1

        return result
