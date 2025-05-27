from imports import *

class Solution:
    def hIndex(self, citations: List[int]) -> int:        
        n = len(citations)
        citations.sort(reverse = True)
        citations_count = Counter(citations)

        count = 0

        for i in range(citations[0], -1, -1):
            if citations_count[i] is not None:
                count += citations_count[i]

            if count >= i:
                return i
        
        return count
