class Solution:
    def countValidSubstrings(self, s: str) -> int:
        result, a, ab, abc = 0, -1, -1, -1
        for i, c in enumerate(s):
            if c == 'a':
                a = i
            elif c == 'b' and a != -1:
                ab = a
            elif c == 'c' and ab != -1:
                abc = ab
            
            result += i - abc

        return result
