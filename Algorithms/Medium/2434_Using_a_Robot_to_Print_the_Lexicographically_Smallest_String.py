from imports import *

class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        stack = []
        result = []
        min_char = "a"

        for c in s:
            stack.append(c)
            count[c] -= 1
            
            while min_char != "z" and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())
        
        return "".join(result)
