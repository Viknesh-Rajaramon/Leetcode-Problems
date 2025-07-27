class Solution:
    def numOfSubsequences(self, s: str) -> int:
        t = s.count("T")
        l, c, lc, ct = 0, 0, 0, 0

        m, r, ts = 0, 0, 0
        for ch in s:
            if ch == "L":
                l += 1
            elif ch == "C":
                c += 1
                lc += l
            elif ch == "T":
                r += lc
                ct += c
                ts += 1
            
            rem = t - ts
            g = l * rem
            if g > m:
                m = g
        
        m = max(m, l * (t - ts))
        return r + max(0, lc, ct, m)
