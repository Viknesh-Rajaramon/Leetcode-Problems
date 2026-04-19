class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        half = len(s) // 2
        return sum(s[ : half].count(v) for v in vowels) == sum(s[half : ].count(v) for v in vowels)
