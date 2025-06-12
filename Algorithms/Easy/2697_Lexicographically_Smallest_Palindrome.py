class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        l, r = 0, n-1
        
        result = []
        while l < r:
            if s[l] > s[r]:
                result.append(s[r])
            else:
                result.append(s[l])

            l += 1
            r -= 1
        
        result = "".join(result)
        return result + s[n//2] + result[::-1] if n % 2 else result + result[::-1]
