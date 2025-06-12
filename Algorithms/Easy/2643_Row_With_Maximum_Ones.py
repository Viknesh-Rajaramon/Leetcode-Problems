from imports import *

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result = [0, 0]
        for i in range(len(mat)):
            count = sum(mat[i])
            if count > result[1]:
                result[0] = i
                result[1] = count

        return result
