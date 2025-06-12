class Solution:
    def minimumChairs(self, s: str) -> int:
        result, chairs = 0, 0
        for c in s:
            if c == "E":
                if chairs == 0:
                    result += 1
                else:
                    chairs += 1
            else:
                chairs -= 1

        return result
