class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ""
        
        result, r = ['9'] * (sum//9), sum%9
        if r > 0:
            result.append(str(r))
        
        result += ['0'] * (num - len(result))
        return "".join(result)
