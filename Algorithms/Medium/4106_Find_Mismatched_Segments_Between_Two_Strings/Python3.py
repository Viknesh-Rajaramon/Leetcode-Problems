class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        result, n, i = [], len(s1), 0
        while i < n:
            if s1[i] == s2[i]:
                i += 1
                continue

            start = i
            while i < n and s1[i] != s2[i]:
                i += 1
                
            result.append([s1[start : i], s2[start : i]])

        return result
