class Solution:
    def toLowerCase(self, s: str) -> str:
        new_str = []
        for c in s:
            if ord("A") <= ord(c) <= ord("Z"):
                new_str.append(chr(ord(c) - ord("A") + ord("a")))
            else:
                new_str.append(c)
        
        return "".join(new_str)
