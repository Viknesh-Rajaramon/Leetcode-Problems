class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True
        
        def almost_palindrome(left: int, right: int) -> bool:
            while left < right and s[left] == s[right]:
                left += 1
                right -= 1
            
            if left >= right:
                return True
            
            return is_palindrome(left+1, right) or is_palindrome(left, right-1)
        
        def good(k: int) -> bool:
            for i in range(n-k+1):
                if almost_palindrome(i, i+k-1):
                    return True
            
            return False
        
        left, right = 1, (n+2)//2
        while right-left > 1:
            mid = (left+right) // 2
            if good(2*mid):
                left = mid
            else:
                right = mid
        
        result = 2*left
        left, right = 0, (n+2)//2
        while right-left > 1:
            mid = (left+right) // 2
            if good(2*mid+1):
                left = mid
            else:
                right = mid

        return max(result, 2*left + 1)
