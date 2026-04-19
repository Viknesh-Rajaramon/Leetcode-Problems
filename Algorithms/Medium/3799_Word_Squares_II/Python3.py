from typing import List
from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for word in words:
            word_map[word[0]].append(word)

        result = []
        for top in words:
            for left in word_map[top[0]]:
                if top == left:
                    continue

                for right in word_map[top[3]]:
                    if right == top or right == left:
                        continue

                    for bottom in word_map[left[3]]:
                        if bottom[3] != right[3]:
                            continue

                        if bottom == top or bottom == left or bottom == right:
                            continue

                        result.append([top, left, right, bottom])
        
        return sorted(result)
