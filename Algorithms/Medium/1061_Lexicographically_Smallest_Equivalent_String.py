from typing import List
from collections import defaultdict, deque

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        edges = defaultdict(set)
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                edges[c1].add(c2)
                edges[c2].add(c1)
        
        lex_mapping = {}
        for c in edges.keys():
            if c in lex_mapping:
                continue

            visited = set([c])
            queue = deque([c])

            while queue:
                char = queue.popleft()
                
                for eq_char in edges[char]:
                    if eq_char not in visited:
                        queue.append(eq_char)
                        visited.add(eq_char)
            
            visited = sorted(visited)
            for char in visited:
                lex_mapping[char] = visited[0]
        
        result = []
        for c in baseStr:
            char = lex_mapping[c] if c in lex_mapping else c
            result.append(char)
        
        return "".join(result)
