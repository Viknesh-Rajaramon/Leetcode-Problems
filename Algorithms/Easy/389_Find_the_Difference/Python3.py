class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = [0 for _ in range(26)]
        t_map = [0 for _ in range(26)]

        for c in s:
            i = ord(c) - ord("a")
            s_map[i] += 1

        for c in t:
            i = ord(c) - ord("a")
            t_map[i] += 1
        
        c = ""
        for i in range(26):
            if s_map[i] != t_map[i]:
                c = chr(i + ord("a"))
                break

        return c
