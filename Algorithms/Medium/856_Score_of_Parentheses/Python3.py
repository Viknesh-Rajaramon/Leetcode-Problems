class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result, depth = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    result += 1<<depth

        return result
