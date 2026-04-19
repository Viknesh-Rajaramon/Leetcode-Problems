from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = "aeiou"
        
        exact_words, capitalization, vowel_error = set(wordlist), {}, {}
        for w in wordlist:
            l = w.lower()
            if l not in capitalization:
                capitalization[l] = w

            pattern = []
            for c in l:
                if c in vowels:
                    pattern.append("*")
                else:
                    pattern.append(c)
            
            p = "".join(pattern)
            if p not in vowel_error:
                vowel_error[p] = w


        result = []
        for q in queries:
            w = q.lower()
            if q in exact_words:
                result.append(q)
            elif w in capitalization:
                result.append(capitalization[w])
            else:
                pattern = []
                for c in w:
                    if c in vowels:
                        pattern.append("*")
                    else:
                        pattern.append(c)
                
                p = "".join(pattern)
                if p in vowel_error:
                    result.append(vowel_error[p])
                else:
                    result.append("")

        return result
