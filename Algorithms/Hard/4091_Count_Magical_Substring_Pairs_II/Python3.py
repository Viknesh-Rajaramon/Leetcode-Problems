class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        l, r, pos = [[0] * 27 for _ in range(n)], [[0] * 27 for _ in range(n)], [-1] * 26
        for i in range(n):
            pos[ord(s[i])-97] = i
            p = sorted((x for x in pos if x != -1), reverse = True)
            for k in range(len(p)):
                l[i][k+1] = p[k] - (p[k+1] if k+1 < len(p) else -1)
        
        pos = [n] * 26
        for i in range(n-1, -1, -1):
            pos[ord(s[i])-97] = i
            q = sorted(x for x in pos if x != n)
            for k in range(len(q)):
                r[i][k+1] = (q[k+1] if k+1 < len(q) else n) - q[k]
        
        result = 0
        for i in range(n-1):
            for k in range(1, 27):
                result += l[i][k] * r[i+1][k]

        return result
