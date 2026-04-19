class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def all_caps(word: str) -> bool:
            for c in word:
                if not (ord("A") <= ord(c) <= ord("Z")):
                    return False
            
            return True

        def all_small(word: str) -> bool:
            if word == "":
                return True
            
            for c in word:
                if not (ord("a") <= ord(c) <= ord("z")):
                    return False
            
            return True

        def only_first(word: str) -> bool:
            return all_caps(word[0]) and all_small(word[1:])
        
        return all_caps(word) or all_small(word) or only_first(word)
