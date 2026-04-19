from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        learned, users, known = list(map(set, languages)), set(), defaultdict(int)
        def can_communicate(x: int):
            if x in users:
                return
            
            users.add(x)
            for lang in languages[x]:
                known[lang] += 1

        for (u, v) in friendships:
            if learned[u-1].isdisjoint(learned[v-1]):
                can_communicate(u-1)
                can_communicate(v-1)
        
        return len(users) - max(known.values(), default=0)
