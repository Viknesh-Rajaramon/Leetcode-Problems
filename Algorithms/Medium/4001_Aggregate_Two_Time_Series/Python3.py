class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        result, m, n, i, j = [], len(series1), len(series2), 0, 0
        while i < m and j < n:
            if series1[i][0] == series2[j][0]:
                result.append([series1[i][0], series1[i][1] + series2[j][1]])
                i += 1
                j += 1
            elif series1[i][0] < series2[j][0]:
                result.append([series1[i][0], series1[i][1] + series2[j][1]])
                i += 1
            else:
                result.append([series2[j][0], series1[i][1] + series2[j][1]])
                j += 1
        
        while i < m:
            result.append(series1[i])
            i += 1
        
        while j < n:
            result.append(series2[j])
            j += 1

        return result
