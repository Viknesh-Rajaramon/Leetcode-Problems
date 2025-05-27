class Solution:
    solutions = ["1"]
    
    def countAndSay(self, n: int) -> str:
        if n <= len(Solution.solutions):
            return Solution.solutions[n-1]
        
        s = self.countAndSay(n-1)
        count = 1
        c = s[0]
        result = []
        for i in range(1, len(s)):
            if s[i] == c:
                count += 1
            else:
                result.append(str(count))
                result.append(c)
                c = s[i]
                count = 1
            
        result.append(str(count))
        result.append(c)
        Solution.solutions.append("".join(result))
        return Solution.solutions[-1]
