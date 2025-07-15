class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        vowel, consonant = False, False
        for c in word:
            if c.isalpha():
                if c in vowels:
                    vowel = True
                else:
                    consonant = True
            elif c.isdigit():
                pass
            else:
                return False
        
        if not vowel or not consonant:
            return False

        return True
