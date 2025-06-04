from imports import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack or stack[-1] * a > 0:
                stack.append(a)
            else:
                added = False
                while stack:
                    if stack[-1] < 0:
                        stack.append(a)
                        added = True
                        break
                    else:
                        val = abs(a)
                        if stack[-1] == val:
                            stack.pop()
                            added = True
                            break
                        elif stack[-1] > val:
                            added = True
                            break
                        else:
                            stack.pop()
                
                if not added:
                    stack.append(a)

        return stack
