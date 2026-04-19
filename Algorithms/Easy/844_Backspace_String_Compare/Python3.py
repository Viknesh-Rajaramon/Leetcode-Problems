class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []

        for c in s:
            if c == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(c)

        for c in t:
            if c == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(c)
        
        return stack1 == stack2
