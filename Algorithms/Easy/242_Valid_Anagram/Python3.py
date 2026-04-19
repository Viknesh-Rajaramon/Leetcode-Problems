class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = [0 for _ in range(26)]
        t_letters = [0 for _ in range(26)]

        for c in s:
            i = ord(c) - ord('a')
            s_letters[i] += 1

        for c in t:
            i = ord(c) - ord('a')
            t_letters[i] += 1
        
        return s_letters == t_letters
