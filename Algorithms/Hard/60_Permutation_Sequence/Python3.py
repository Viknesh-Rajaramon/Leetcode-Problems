from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result, digits, factor = [], list(range(1, n+1)), factorial(n-1)
        k -= 1
        for m in range(n-1, 0, -1):
            i = k//factor
            result.append(str(digits[i]))
            digits.pop(i)
            k %= factor
            factor //= m

        result.append(str(digits[0]))
        return "".join(result)
