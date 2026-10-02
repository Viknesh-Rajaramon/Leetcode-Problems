class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = {}
        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []
            
            pos[num].append(i)
        
        result = 0
        for indices in pos.values():
            if len(indices) == 3 and 2*indices[1] == indices[0] + indices[2]:
                result += 1

        return result
