class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        prev_row, curr_row = [""] * (m+1), [""] * (m+1)
        
        for j in range(m):
            prev_row[j] = str2[j:]

        for i in range(n-1, -1, -1):
            curr_row = [""] * (m+1)
            curr_row[-1] = str1[i:]

            for j in range(m-1, -1, -1):
                if str1[i] == str2[j]:
                    curr_row[j] = str1[i] + prev_row[j+1]
                elif len(curr_row[j+1]) < len(prev_row[j]):
                    curr_row[j] = str2[j] + curr_row[j+1]
                else:
                    curr_row[j] = str1[i] + prev_row[j]

            prev_row = curr_row
    
        return curr_row[0]
