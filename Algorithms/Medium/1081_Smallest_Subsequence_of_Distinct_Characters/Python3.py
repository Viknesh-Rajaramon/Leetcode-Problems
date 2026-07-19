class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visited, freq = set(), {}
        for c in s:
            if c not in freq:
                freq[c] = 0

            freq[c] += 1
        
        result = []
        for c in s:
            freq[c] -= 1
            if c in visited:
                continue
            
            while result and result[-1] > c and freq[result[-1]] > 0:
                visited.remove(result.pop())
            
            result.append(c)
            visited.add(c)

        return "".join(result)
