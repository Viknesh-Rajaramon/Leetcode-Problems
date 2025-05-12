from imports import *

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = deque()
        n = len(part)
        
        for c in s:
            stack.append(c)

            if len(stack) >= n:
                count = 0
                letters = deque()
                while count < n:
                    letters.appendleft(stack.pop())
                    if letters[0] != part[n-1-count]:
                        stack.extend(letters)
                        break
                    else:
                        count += 1
        
        return "".join(c for c in stack)
