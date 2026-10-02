class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos = {}
        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []
            
            pos[num].append(i)
        
        result = 0
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            special, diff = True, indices[1] - indices[0]
            for i in range(1, len(indices)-1):
                if indices[i+1] - indices[i] != diff:
                    special = False
                    break
            
            if special:
                result += 1

        return result
