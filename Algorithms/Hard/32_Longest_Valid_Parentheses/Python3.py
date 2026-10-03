class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result, stack = 0, [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i-stack[-1])
        
        return result
