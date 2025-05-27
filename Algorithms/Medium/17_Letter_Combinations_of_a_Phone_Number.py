from imports import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        n = len(digits)
        ans = letter_map[digits[0]]
        for i in range(1, n):
            temp = []
            letters = letter_map[digits[i]]
            
            for x in ans:
                for l in letters:
                    temp.append(x+l)
            
            ans = temp
        
        return ans
