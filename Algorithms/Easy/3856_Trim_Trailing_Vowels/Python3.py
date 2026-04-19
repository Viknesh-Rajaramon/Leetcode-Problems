class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        result = list(s)
        while result and result[-1] in "aeiou":
            result.pop()
        
        return "".join(result)
