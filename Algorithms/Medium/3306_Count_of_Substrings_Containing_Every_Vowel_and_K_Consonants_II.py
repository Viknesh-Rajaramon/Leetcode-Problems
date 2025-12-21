from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def atleast_k(k: int) -> int:
            vowel = defaultdict(int)
            ans = 0
            consonants = 0
            l = 0

            for r in range(n):
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    consonants += 1
                
                while len(vowel) == 5 and consonants >= k:
                    ans += len(word) - r
                    if word[l] in vowel:
                        vowel[word[l]] -= 1
                    else:
                        consonants -= 1
                    
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    
                    l += 1

            return ans
        
        return atleast_k(k) - atleast_k(k+1)
