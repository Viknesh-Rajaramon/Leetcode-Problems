from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_index = defaultdict(list)

        for i, c in enumerate(s):
            char_index[c].append(i)
        
        for c, indices in char_index.items():
            if len(indices) == 1:
                return indices[0]
        
        return -1
