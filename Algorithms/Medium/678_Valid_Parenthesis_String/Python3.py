class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count, closed_count, n = 0, 0, len(s)-1
        for i in range(n+1):
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            if s[n-i] == ')' or s[n-i] == '*':
                closed_count += 1
            else:
                closed_count -= 1
            
            if open_count < 0 or closed_count < 0:
                return False

        return True
