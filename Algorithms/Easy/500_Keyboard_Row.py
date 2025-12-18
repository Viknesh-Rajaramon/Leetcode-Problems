from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        char_rows = {}
        for i, chars in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
            for c in chars:
                char_rows[c] = i+1
        
        result = []
        for word in words:
            row = char_rows[word[0].lower()]
            flag = True

            for i in range(1, len(word)):
                if row != char_rows[word[i].lower()]:
                    flag = False
                    break
            
            if flag:
                result.append(word)
        
        return result
