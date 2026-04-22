class Solution:
    def partitionString(self, s: str) -> int:
        result, seen = 1, set()
        for c in s:
            if c in seen:
                result += 1
                seen = set()
            
            seen.add(c)

        return result
