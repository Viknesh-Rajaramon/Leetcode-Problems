class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0 or num % 10 != 0:
            return True
        
        return False
