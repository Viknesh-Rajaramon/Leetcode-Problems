class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        result, right = n, n-1
        for i in range(n-2, -1, -1):
            if position[i+1] - position[i] <= distance or speed[i] > speed[right]:
                result -= 1
            else:
                right = i

        return result
