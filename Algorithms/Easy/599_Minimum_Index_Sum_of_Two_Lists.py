from imports import *

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words = {}
        for i, word in enumerate(list1):
            words[word] = i
        
        result, min_index_sum = [], inf
        for i, word in enumerate(list2):
            if word in words:
                index_sum = i + words[word]
                if index_sum < min_index_sum:
                    result = [word]
                    min_index_sum = index_sum
                elif index_sum == min_index_sum:
                    result.append(word)
        
        return result
