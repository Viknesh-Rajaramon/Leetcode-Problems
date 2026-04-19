class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        stack = [s[0], s[1]]
        for c in s[2 : ]:
            if c == stack[-1] and c == stack[-2]:
                continue
            
            stack.append(c)
        
        return "".join(stack)
