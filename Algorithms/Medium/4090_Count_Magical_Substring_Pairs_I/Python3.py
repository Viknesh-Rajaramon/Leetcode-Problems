class Solution:
    def countMagicalPairs(self, s: str) -> int:
        result, n = 0, len(s)
        for j in range(n-1):
            r, hs = [0] * 27, set()
            for k in range(j+1, n):
                hs.add(s[k])
                r[len(hs)] += 1

            hs.clear()
            for i in range(j, -1, -1):
                hs.add(s[i])
                result += r[len(hs)]

        return result
