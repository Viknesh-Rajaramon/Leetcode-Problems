class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        
        first, second = "a", "b"
        big, small = x, y
        if x < y:
            first, second = second, first
            big, small = small, big

        stack = []
        for c in s:
            if stack and first == stack[-1] and second == c:
                stack.pop()
                score += big
            else:
                stack.append(c)
        
        stack2 = []
        for c in stack:
            if stack2 and first == c and second == stack2[-1]:
                stack2.pop()
                score += small
            else:
                stack2.append(c)

        return score
