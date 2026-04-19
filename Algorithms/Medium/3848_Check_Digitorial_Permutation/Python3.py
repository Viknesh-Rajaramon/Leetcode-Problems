class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        def fact(digit: str) -> int:
            result = 1
            for i in range(2, int(digit)+1):
                result *= i

            return result
        
        n = str(n)
        if len(n) not in {1, 3, 5}:
            return False
        
        return sorted(str(sum(map(fact, n)))) == sorted(n)
