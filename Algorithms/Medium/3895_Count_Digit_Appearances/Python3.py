class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return "".join(map(str, nums)).count(str(digit))
