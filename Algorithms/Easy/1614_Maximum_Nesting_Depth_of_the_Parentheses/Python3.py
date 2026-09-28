class Solution:
    def maxDepth(self, s: str) -> int:
        result, curr = 0, 0
        for c in s:
            if c == '(':
                curr += 1
                result = max(result, curr)
            elif c == ')':
                curr -= 1
        
        return result
