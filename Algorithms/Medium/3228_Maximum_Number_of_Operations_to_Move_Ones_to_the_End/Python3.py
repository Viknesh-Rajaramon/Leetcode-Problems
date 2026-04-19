class Solution:
    def maxOperations(self, s: str) -> int:
        result, tot, ones = 0, 0, [len(i) for i in s.split("0") if i]
        if not ones:
            return 0
        
        for f in ones[:-1]:
            tot += f
            result += tot

        return result if s[-1] == "1" else result + tot + ones[-1]
