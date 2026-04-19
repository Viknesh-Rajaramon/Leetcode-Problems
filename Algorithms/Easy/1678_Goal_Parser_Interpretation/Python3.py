class Solution:
    def interpret(self, command: str) -> str:
        stack = []

        for c in command:
            if c == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append("o")
                else:
                    stack.pop(-3)
            else:
                stack.append(c)

        return "".join(stack)
