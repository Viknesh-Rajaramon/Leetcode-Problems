class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0
        for ch in s:
            if ch.isalpha():
                if ch in "aeiou":
                    v += 1
                else:
                    c += 1
        
        return v // c if c > 0 else 0
