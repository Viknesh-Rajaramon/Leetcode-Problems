class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        ones = [0] * (n+1)

        for i in reversed(range(n)):
            if s[i] == "1":
                ones[i] = ones[i+1]+1
            else:
                ones[i] = ones[i+1]
        
        count = 0
        result = max(ones[1:])
        for i in range(n-1):
            if s[i] == "0":
                count += 1
                result = max(result, count + ones[i+1])
        
        return result
