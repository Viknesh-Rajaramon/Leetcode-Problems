class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        ord_a = ord("a")
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue

            prev_char = chr(ord_a + ((ord(c) - ord_a + 25) % 26))
            next_char = chr(ord_a + ((ord(c) - ord_a + 1) % 26))
            if stack[-1] == prev_char or stack[-1] == next_char:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
