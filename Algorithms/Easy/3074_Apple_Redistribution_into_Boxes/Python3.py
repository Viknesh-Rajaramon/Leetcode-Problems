from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total_apples = sum(apple)
        
        for i, cap in enumerate(capacity):
            total_apples -= cap
            if total_apples <= 0:
                return i+1
