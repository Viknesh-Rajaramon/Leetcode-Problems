class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(list(map(int, str(n))))
