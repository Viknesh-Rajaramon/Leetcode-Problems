class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1] = (c, stack[-1][1] + 1)
            else:
                stack.append((c, 1))
            
            while len(stack) >= 2 and stack[-2][0] == "(" and stack[-2][1] >= k and stack[-1][0] == ")" and stack[-1][1] >= k:
                stack[-2] = ("(", stack[-2][1] - k)
                stack[-1] = (")", stack[-1][1] - k)

                if stack[-1][1] == 0:
                    stack.pop()
                    
                if stack[-1][1] == 0:
                    stack.pop()
                    
                if len(stack) >= 2 and stack[-2][0] == stack[-1][0]:
                    stack[-2] = (stack[-2][0], stack[-2][1] + stack[-1][1])
                    stack.pop()

        return "".join([c * count for c, count in stack])
