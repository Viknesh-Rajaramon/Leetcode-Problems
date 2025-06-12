from imports import *

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items_ = defaultdict(int)
        for value, weight in items1:
            items_[value] += weight
        
        for value, weight in items2:
            items_[value] += weight
        
        return sorted(items_.items())
