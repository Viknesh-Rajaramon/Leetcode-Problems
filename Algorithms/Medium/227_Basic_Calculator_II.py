import string

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = "+"

        for c in s+"\0":
            if c == " ":
                continue
            elif c in string.digits:
                num = num*10 + int(c)
            else:
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                prev_op = c
                num = 0
        
        return sum(stack)
