class Solution:
    def minSwaps(self, s: str) -> int:
        open_bracs = 0
        for i in range(len(s)):
            if s[i] == "[":
                open_bracs += 1
            elif s[i] == "]" and open_bracs > 0:
                open_bracs -= 1
            else:
                pass
        
        return (open_bracs + 1) // 2
