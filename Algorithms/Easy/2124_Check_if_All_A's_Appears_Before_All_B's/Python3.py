class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        for c in s:
            if c == 'a' and seen_b:
                return False
            elif c == 'b':
                seen_b = True

        return True
