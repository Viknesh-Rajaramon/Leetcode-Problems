class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        n = len(s1)
        index = []

        for i in range(n):
            if s1[i] != s2[i]:
                count += 1
                index.append(i)
        
        if count == 0:
            return True
        
        if count == 2:
            new_str = s1[: index[0]] + s1[index[1]] + s1[index[0]+1 : index[1]] + s1[index[0]] + s1[index[1]+1 : ]

            if new_str == s2:
                return True
        
        return False
