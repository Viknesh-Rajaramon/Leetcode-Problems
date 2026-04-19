class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        for word in text.split(" "):
            for c in brokenLetters:
                if word.count(c) > 0:
                    break
            else:
                result += 1
        
        return result
