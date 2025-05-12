class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        hash_map = {}
        letters_set, words_set = set(), set()
        for i in range(len(pattern)):
            if pattern[i] not in letters_set:
                if words[i] not in words_set:
                    hash_map[pattern[i]] = words[i]
                    letters_set.add(pattern[i])
                    words_set.add(words[i])
                else:
                    return False
            else:
                if hash_map[pattern[i]] == words[i]:
                    continue
                else:
                    return False

        return True
