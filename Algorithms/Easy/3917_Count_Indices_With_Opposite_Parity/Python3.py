class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        result, even, odd = [], 0, 0
        for num in nums[ : : -1]:
            if num & 1:
                result.append(even)
                odd += 1
            else:
                result.append(odd)
                even += 1

        return result[::-1]
