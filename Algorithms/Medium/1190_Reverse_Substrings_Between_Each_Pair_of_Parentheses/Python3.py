class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = [""]
        for c in s:
            if c == '(':
                result.append("")
            elif c == ')':
                temp = result.pop()
                result[-1] += temp[ : : -1]
            else:
                result[-1] += c

        return result[0]
