class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dist(a: int, b: int) -> int:
            d = abs(a-b)
            return min(d, 10-d)

        base = dist(0, int(s[0]))
        for i in range(n-1):
            base += dist(int(s[i]), int(s[i+1]))

        result = min(base, base - dist(0, int(s[0])) + dist(0, int(s[-1])))
        for k in range(n-1):
            result = min(result, base - dist(int(s[k]), int(s[k+1])) + dist(int(s[k]), int(s[-1])))

        return result
