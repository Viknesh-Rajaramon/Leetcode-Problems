class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        m = (n-1)//8 + 1
        return m * (n - 4*(m-1))
