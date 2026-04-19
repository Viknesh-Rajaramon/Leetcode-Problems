class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digit_low = ord("0")
        digit_high = ord("9")

        for c in s:
            digit_c = ord(c)
            if digit_low <= digit_c and digit_c <= digit_high:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(c for c in stack)
