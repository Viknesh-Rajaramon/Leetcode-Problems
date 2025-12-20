from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        counts = sorted([c for c, w in Counter(s).items() if w >= k], reverse = True)

        result = ""
        queue = deque(counts)
        while queue:
            curr = queue.popleft()
            if len(curr) > len(result):
                result = curr
            
            for c in counts:
                nxt = curr + c
                it = iter(s)
                if all(c in it for c in nxt*k):
                    queue.append(nxt)
        
        return result
