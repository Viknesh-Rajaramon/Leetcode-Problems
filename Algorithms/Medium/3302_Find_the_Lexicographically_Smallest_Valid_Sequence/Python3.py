from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        last, j = [0] * n, n-1
        for i in range(m-1, -1, -1):
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
                if j < 0:
                    break
        
        result, skip, j = [], False, 0
        for i in range(m):
            if j == n:
                break
            
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            else:
                if not skip and (j == n-1 or last[j+1] > i):
                    skip = True
                    result.append(i)
                    j += 1

        return result if j == n else []
