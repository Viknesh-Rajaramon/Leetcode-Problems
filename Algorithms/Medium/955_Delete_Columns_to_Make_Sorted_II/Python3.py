from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result, m, n = 0, len(strs), len(strs[0])
        is_correct = [False] * (m-1)
        for j in range(n):
            correct = True
            for i in range(m-1):
                if not is_correct[i] and strs[i][j] > strs[i+1][j]:
                    correct = False
                    break
            
            if not correct:
                result += 1
                continue
            
            for i in range(m-1):
                if not is_correct[i] and strs[i][j] < strs[i+1][j]:
                    is_correct[i] = True

        return result
