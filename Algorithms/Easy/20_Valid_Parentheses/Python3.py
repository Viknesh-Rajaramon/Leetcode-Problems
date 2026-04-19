class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for c in s:
            if c in bracket.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or bracket[stack.pop()] != c:
                    return False
        
        if len(stack) > 0:
            return False

        return True
