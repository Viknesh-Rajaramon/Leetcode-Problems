class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        count = sum // 9
        remaining = sum - count * 9

        result = "9" * count
        if remaining != 0:
            result += str(remaining)
        
        if len(result) > num:
            return ""
        
        result += "0" * (num - len(result))
        return result
