class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pos = [0] * (n+1)
        for i in range(n):
            if i == 0 or s[i-1] == "0":
                pos[i+1] = i
            else:
                pos[i+1] = pos[i]
        
        result = 0
        for i in range(1, n+1):
            count_0, j = 1 if s[i-1] == "0" else 0, i
            while j > 0 and count_0 * count_0 <= n:
                diff = i - pos[j] - (count_0 * (count_0 + 1))
                if diff >= 0:
                    result += min(j - pos[j], diff + 1)
                
                j = pos[j]
                count_0 += 1

        return result
