class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid

            if sqr == x:
                return mid
            elif sqr < x:
                low = mid + 1
            else:
                high = mid - 1

        return high
