class Solution:
    def minInsertions(self, s: str) -> int:
        result, n, left_count, i = 0, len(s), 0, 0
        while i < n:
            if s[i] == '(':
                left_count += 1
            else:
                if left_count > 0:
                    left_count -= 1
                else:
                    result += 1
                
                if i+1 < n and s[i+1] == ')':
                    i += 1
                else:
                    result += 1
            
            i += 1

        result += 2*left_count
        return result
