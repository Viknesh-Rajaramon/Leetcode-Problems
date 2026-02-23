class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        req = 1 << k
        seen, mask, h = [False] * req, req - 1, 0
        for i, c in enumerate(s):
            h = ((h << 1) & mask) | (ord(c) & 1)
            if i >= k-1 and not seen[h]:
                seen[h] = True
                req -= 1
                if req == 0:
                    return True

        return False
