class Solution:
    def countMonobit(self, n: int) -> int:
        result, num = 0, 0
        while num <= n:
            num = (num << 1) + 1
            result += 1

        return result
