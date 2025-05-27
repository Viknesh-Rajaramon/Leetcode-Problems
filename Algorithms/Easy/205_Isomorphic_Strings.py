class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings_s, mappings_t = {}, {}

        for a, b in zip(s, t):
            if a in mappings_s:
                if mappings_s[a] != b:
                    return False
            
            if b in mappings_t:
                if mappings_t[b] != a:
                    return False

            mappings_s[a] = b
            mappings_t[b] = a
            
        return True
