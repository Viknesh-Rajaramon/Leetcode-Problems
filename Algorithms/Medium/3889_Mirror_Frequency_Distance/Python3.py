from collections import Counter

class Solution:
    def mirrorFrequency(self, s: str) -> int:
        result, freq, visited = 0, Counter(s), set()
        for c in s:
            if c in visited:
                continue
            
            m = chr(105 - ord(c)) if "0" <= c <= "9" else chr(219 - ord(c))
            visited.add(c)
            visited.add(m)

            result += abs(freq[c] - freq[m])

        return result
