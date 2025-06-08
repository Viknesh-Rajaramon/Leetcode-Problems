from imports import *

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp_letters = defaultdict(int)
        for c in licensePlate:
            if c in string.ascii_letters:
                lp_letters[c.lower()] += 1
        
        result = ""
        for word in words:
            flag = True
            for c, count in lp_letters.items():
                if word.count(c) < count:
                    flag = False
                    break
            
            if flag:
                if result == "" or len(word) < len(result):
                    result = word
        
        return result
