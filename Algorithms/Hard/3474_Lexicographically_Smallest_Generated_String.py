class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        result, fixed, j = ["a"] * (n+m-1), [-1] * (n+m-1), m
        for i in range(n+m-1):
            if i < n and str1[i] == "T":
                j = 0
            
            if j < m:
                result[i], fixed[i] = str2[j], j
            
            j += 1

        j, lps = 0, [0]
        for i in range(1, m):
            while j and str2[j] != str2[i]:
                j = lps[j-1]
            
            if str2[j] == str2[i]:
                j += 1
            
            lps.append(j)
        
        j, last = 0, -1
        for i, ch in enumerate(result):
            if fixed[i] == -1:
                last = i
            
            while j and (j == m or str2[j] != ch):
                j = lps[j-1]
            
            if str2[j] == ch:
                j += 1
            
            if i >= m-1:
                if str1[i-m+1] == 'T' and j < m:
                    return ""
                
                if str1[i-m+1] == 'F' and j == m: 
                    if last < i-m+1:
                        return ""
                    
                    result[last], j = "b", fixed[i]+1 if fixed[i] != -1 else 0

        return "".join(result)
