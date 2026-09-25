class Solution:
    def isPalindromic(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            for bit in range(7, -1, -1):
                left, right = (ord(s[l]) >> bit) & 1, (ord(s[r]) >> (7 - bit)) & 1
                if left != right:
                    return False

            l += 1
            r -= 1

        return True
