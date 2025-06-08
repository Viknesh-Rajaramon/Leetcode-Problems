class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        key = s.replace("-", "").upper()
        n = len(key)
        result = []
        
        start = n % k
        if start != 0:
            result.append(key[:start])
        
        for i in range(start, n, k):
            result.append(key[i : i+k])

        return "-".join(result)
