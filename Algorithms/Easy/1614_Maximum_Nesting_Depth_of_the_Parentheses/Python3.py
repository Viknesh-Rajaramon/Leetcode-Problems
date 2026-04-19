class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0
        for c in s:
            if c == "(":
                stack.append("(")
                result = max(result, len(stack))
            elif c == ")":
                stack.pop()
        
        return result
