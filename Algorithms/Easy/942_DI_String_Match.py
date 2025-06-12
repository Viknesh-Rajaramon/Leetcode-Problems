from imports import *

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)

        result = []
        for c in s:
            if c == "D":
                result.append(right)
                right -= 1
            else:
                result.append(left)
                left += 1

        result.append(left)
        return result
