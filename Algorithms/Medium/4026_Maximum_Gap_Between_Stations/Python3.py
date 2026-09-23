class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        m, n = len(station), len(skill)
        left, right, i = [0] * n, [0] * n, 0
        for j in range(n):
            while i < m and station[i] != skill[j]:
                i += 1

            left[j] = i
            i += 1
        
        i = m-1
        for j in range(n-1, -1, -1):
            while i >= 0 and station[i] != skill[j]:
                i -= 1
            
            right[j] = i
            i -= 1
        
        result = 0
        for i in range(n-1):
            result = max(result, right[i+1] - left[i])

        return result
