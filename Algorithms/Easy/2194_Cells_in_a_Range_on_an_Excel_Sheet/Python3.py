from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        for i in range(ord(s[0]), ord(s[3])+1):
            c = chr(i)
            for j in range(int(s[1]), int(s[4])+1):
                result.append(c+str(j))
        
        return result
