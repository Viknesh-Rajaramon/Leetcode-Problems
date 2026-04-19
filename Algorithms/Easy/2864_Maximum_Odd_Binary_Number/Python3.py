class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        no_of_ones = s.count("1")
        return "1" * (no_of_ones - 1) + "0" * (len(s) - no_of_ones) + "1"
