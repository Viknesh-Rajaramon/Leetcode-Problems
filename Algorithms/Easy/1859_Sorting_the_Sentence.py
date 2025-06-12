class Solution:
    def sortSentence(self, s: str) -> str:
        result = sorted(s.split(" "), key = lambda x: int(x[-1]))
        return " ".join(word[ : -1] for word in result)
