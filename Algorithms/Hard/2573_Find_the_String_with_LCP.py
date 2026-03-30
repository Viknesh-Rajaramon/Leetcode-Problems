from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        result, curr = [""] * n, 97
        for i in range(n):
            if result[i] != "":
                continue

            if curr > 122:
                return ""
                
            result[i] = chr(curr)
            for j in range(i+1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                
                if lcp[i][j] == 0:
                    continue
                
                result[j] = result[i]
                
            curr += 1
        
        for i in range(n):
            for j in range(i, n):
                if result[i] != result[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n-1 or j == n-1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i+1][j+1]+1:
                            return ""

        return "".join(result)
