class Solution:
    def partitionString(self, s: str) -> int:
        res = []
        temp = []

        for c in s:
            if c in temp:
                res.append(temp)
                temp = [c]
            else:
                temp.append(c)

        return len(res) + 1
