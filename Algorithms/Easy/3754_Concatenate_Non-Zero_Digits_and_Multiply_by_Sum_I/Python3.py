class Solution:
    def sumAndMultiply(self, n: int) -> int:
        result, digits = 0, list(map(int, str(n)))
        for d in digits:
            if d != 0:
                result = result*10 + d

        return result * sum(digits)
