from imports import *

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        def solve(cnt: List[int], have: int) -> int:
            s = sum(cnt)
            return min((s+have)//2, s-max(0, max(cnt)-have)) if s != 0 else 0
        
        a = ord("a")
        x = ord(x) - a
        c1, c2, both = [0] * 10, [0] * 10, 0
        for card in cards:
            b, c = ord(card[0]) - a, ord(card[1]) - a
            if b == x and c == x:
                both += 1
            elif b == x:
                c1[c] += 1
            elif c == x:
                c2[b] += 1
        
        result = 0
        for i in range(both+1):
            result = max(result, solve(c1, i) + solve(c2, both-i))
        
        return result
