from math import ceil

class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        result, resources = 0, k
        for num in nums:
            if resources < num:
                i = ceil((num - resources)/k)
                resources += i*k
                result += i
            
            resources -= num

        return (result*(result+1)//2) % 1000000007
