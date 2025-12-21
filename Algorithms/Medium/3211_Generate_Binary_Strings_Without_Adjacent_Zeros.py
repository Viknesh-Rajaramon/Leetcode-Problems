from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        
        valid_strings = self.validStrings(n-1)

        result = []
        for num in valid_strings:
            for i in ["0", "1"]:
                if num[-1] == "0" and i == "0":
                    continue
                
                result.append(num + i)

        return result
