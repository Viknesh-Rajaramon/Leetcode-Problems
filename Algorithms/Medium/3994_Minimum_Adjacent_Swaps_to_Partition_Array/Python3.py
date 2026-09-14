class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        result, count_1, count_2 = 0, 0, 0
        for num in nums:
            if num < a:
                result += count_1 + count_2
            elif num > b:
                count_2 += 1
            else:
                count_1 += 1
                result += count_2

        return result % 1000000007
