class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num

        while low <= high:
            mid = (low + high) // 2
            power = mid * mid
            
            if power == num:
                return True
            elif num < power:
                high = mid - 1
            elif num > power:
                low = mid + 1

        return False
