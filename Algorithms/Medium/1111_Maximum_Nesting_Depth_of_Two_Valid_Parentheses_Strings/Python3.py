class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = []
        for i, c in enumerate(seq):
            if c == '(':
                result.append(i%2)
            else:
                result.append(1-i%2)

        return result
