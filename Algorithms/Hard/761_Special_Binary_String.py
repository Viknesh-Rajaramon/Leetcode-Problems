class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        result, count, i = [], 0, 0
        for j, c in enumerate(s):
            count += 1 if c == "1" else -1
            if count == 0:
                result.append("1" + self.makeLargestSpecial(s[i+1 : j]) + "0")
                i = j+1

        result.sort(reverse = True)
        return "".join(result)
