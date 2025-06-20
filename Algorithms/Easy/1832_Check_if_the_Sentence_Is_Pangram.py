class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set()
        for c in sentence:
            if c not in s:
                s.add(c)
        
        return len(s) == 26
