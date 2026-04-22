from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def get_distance(word1: str, word2: str) -> bool:
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
                    if count == 3:
                        return False
            
            return True
        
        result = []
        for word1 in queries:
            for word2 in dictionary:
                if get_distance(word1, word2):
                    result.append(word1)
                    break

        return result
