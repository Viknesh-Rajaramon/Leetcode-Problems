from imports import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                break
            elif sum_ > target:
                j -= 1
            else:
                i += 1
        
        return [i+1, j+1]
