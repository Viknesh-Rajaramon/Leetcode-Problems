class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result, open_count = 0, 0
        for c in s:
            if c == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    result += 1
        
        return result + open_count
