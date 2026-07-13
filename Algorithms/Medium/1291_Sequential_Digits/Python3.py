from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        def find(n: int) -> None:
            if n > high:
                return
            
            if n >= low and n <= high:
                result.append(n)
            
            s = n%10
            if s < 9:
                find(n*10 + s + 1)
        
        for i in range(1, 10):
            find(i)

        return sorted(result)
