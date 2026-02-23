class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zeroes = t.count("0")
        ones = len(t) - zeroes

        result = []
        for c in s:
            if (c == "1" and zeroes) or (c == "0" and ones):
                result.append("1")
                zeroes -= c == "1"
                ones -= c == "0"
            else:
                result.append("0")
                zeroes -= c == "0"
                ones -= c == "1"

        return "".join(result)
