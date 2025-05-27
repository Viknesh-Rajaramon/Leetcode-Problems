class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_pos = [-1] * 3
        count = 0

        for i, c in enumerate(s):
            last_pos[ord(c)-ord("a")] = i
            count += 1 + min(last_pos)
        
        return count
