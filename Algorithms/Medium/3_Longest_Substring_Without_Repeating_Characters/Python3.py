class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        max_len = 0

        l = 0
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            
            letters.add(s[r])
            max_len = max(max_len, r - l + 1)
        
        return max_len
