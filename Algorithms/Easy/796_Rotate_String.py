class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if len(goal) != n:
            return False
        
        count = n
        new_s = s
        while count > 0:
            if new_s == goal:
                return True
            
            new_s = new_s[1 : ] + new_s[0]
            count -= 1
        
        return False
