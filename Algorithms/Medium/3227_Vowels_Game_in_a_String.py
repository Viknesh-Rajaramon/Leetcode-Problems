class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        return count != 0
