from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result, seen, count = [], set(), 0
        for a, b in zip(A, B):
            if a in seen:
                count += 1
            else:
                seen.add(a)
            
            if b in seen:
                count += 1
            else:
                seen.add(b)

            result.append(count)

        return result
