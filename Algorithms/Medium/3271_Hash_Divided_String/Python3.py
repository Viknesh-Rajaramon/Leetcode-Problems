class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        ord_a = ord("a")
        for i in range(0, len(s), k):
            hash_ = 0
            for c in s[i : i+k]:
                hash_ += ord(c) - ord_a
            
            result.append(chr(ord_a + (hash_ % 26)))
        
        return "".join(result)
