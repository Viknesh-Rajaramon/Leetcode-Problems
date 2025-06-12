class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        left, count = 0, 0

        for i, c in enumerate(s):
            if c == "(":
                count += 1
            else:
                if count == 1:
                    result.append(s[left+1 : i])
                    left = i+1
                    count = 0
                else:
                    count -= 1
        
        return "".join(result)
