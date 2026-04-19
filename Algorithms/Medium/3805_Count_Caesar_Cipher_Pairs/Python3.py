from typing import List

class Solution:
    def countPairs(self, words: List[str]) -> int:
        def compare_words(word1: str, word2: str) -> bool:
            m = len(word1)
            if m == 1:
                return True
            
            diff = ord(word1[0]) - ord(word2[0])
            if diff < 0:
                diff += 26
            
            for i in range(1, m):
                next_diff = ord(word1[i]) - ord(word2[i])
                if next_diff < 0:
                    next_diff += 26
                
                if next_diff != diff:
                    return False
            
            return True

        graph = {words[0]: 1}
        for word in words[1 : ]:
            for key in graph:
                if compare_words(word, key):
                    graph[key] += 1
                    break
            else:
                graph[word] = 1

        return sum(count*(count-1) for count in graph.values()) >> 1
