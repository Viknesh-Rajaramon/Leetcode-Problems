from collections import deque

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = deque()

        num = ""
        digit = 1
        for c in pattern:
            if c == "I":
                num = num + str(digit)
                while len(stack) > 0:
                    num = num + stack.pop()
            else:
                stack.append(str(digit))
            
            digit += 1
        
        num = num + str(digit)
        while len(stack) > 0:
            num = num + stack.pop()
        
        return num
