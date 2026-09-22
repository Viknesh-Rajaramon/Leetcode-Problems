class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        result, curr = 0, 0
        for r in requests:
            result += abs(r-curr)
            curr = r

        return result
