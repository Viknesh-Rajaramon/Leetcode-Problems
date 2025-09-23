class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        m, n = len(version1), len(version2)
        if m > n:
            version2.extend([0] * (m-n))
        elif m < n:
            version1.extend([0] * (n-m))
        
        for v1, v2 in zip(version1, version2):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
