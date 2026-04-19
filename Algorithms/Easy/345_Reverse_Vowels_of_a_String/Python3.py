class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s = list(s)

        i, j = 0, len(s) - 1
        while i < j:
            i_in_vowels = s[i] in vowels
            j_in_vowels = s[j] in vowels
            
            if i_in_vowels and j_in_vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif i_in_vowels:
                j -= 1
            elif j_in_vowels:
                i += 1
            else:
                i += 1
                j -= 1
        
        return "".join(s)
