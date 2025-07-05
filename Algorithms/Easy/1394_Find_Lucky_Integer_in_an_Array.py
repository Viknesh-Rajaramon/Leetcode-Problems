from imports import *

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = -1
        for num, count in Counter(arr).items():
            if num == count and num > result:
                result = num
        
        return result
