class Solution:
    def scoreBalance(self, s: str) -> bool:
        ord_a = ord("a") - 1
        left, total = 0, sum(ord(c) - ord_a for c in s)
        if total % 2 == 1:
            return False

        total //= 2
        for c in s:
            left += ord(c) - ord_a
            if left == total:
                return True
            elif left > total:
                return False
        
        return False
