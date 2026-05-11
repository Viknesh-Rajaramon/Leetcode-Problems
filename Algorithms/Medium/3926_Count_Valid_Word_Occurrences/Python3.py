from collections import Counter
import re

class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        freq = Counter(re.findall(r'[a-z]+(?:-[a-z]+)*', s))
        return [freq[q] for q in queries]
