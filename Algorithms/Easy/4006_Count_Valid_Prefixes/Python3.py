class Solution:
    def countValidPrefixes(self, s: str) -> int:
        result, ones, zeros = 0, 0, 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                zeros += 1
            
            if abs(zeros - ones) < 2:
                result += 1
        
        return result
