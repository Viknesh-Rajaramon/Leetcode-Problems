class Solution:
    def isValid(self, s: str) -> bool:
        bracket, stack = {'{': '}', '(': ')', '[': ']'}, []
        for c in s:
            if c in bracket.keys():
                stack.append(c)
            else:
                if not stack or bracket[stack.pop()] != c:
                    return False
        
        return not stack
