class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        left, right = 0, 0
        for c in s:
            if c == "L":
                left += 1
            else:
                right += 1
            
            if left == right:
                result += 1
        
        return result
