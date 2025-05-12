class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_dict = {}

        for c in s:
            if c not in char_dict.keys():
                char_dict[c] = 0
            
            char_dict[c] += 1
        
        return len(set(list(char_dict.values()))) == 1
