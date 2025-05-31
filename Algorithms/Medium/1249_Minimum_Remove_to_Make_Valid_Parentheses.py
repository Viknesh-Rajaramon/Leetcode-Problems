class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        result = [""] * n

        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) > 0:
                    result[stack.pop()] = "("
                    result[i] = s[i]
            else:
                result[i] = s[i]
        
        return "".join(result)
