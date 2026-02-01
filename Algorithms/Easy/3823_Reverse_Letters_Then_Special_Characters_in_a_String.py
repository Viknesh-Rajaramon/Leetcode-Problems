class Solution:
    def reverseByType(self, s: str) -> str:
        letters, chars = [], []
        for c in s:
            if c.isalpha():
                letters.append(c)
            else:
                chars.append(c)
        
        return "".join(letters.pop() if c.isalpha() else chars.pop() for c in s)
