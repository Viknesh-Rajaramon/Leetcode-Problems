from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        if numRows == 1:
            return arr

        for i in range(1, numRows):
            rowArr = [1]
            for j in range(1, len(arr[i-1])):
                rowArr.append(arr[i-1][j-1] + arr[i-1][j])
            rowArr.append(1)
            arr.append(rowArr)

        return arr
