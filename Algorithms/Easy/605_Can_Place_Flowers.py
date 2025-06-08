from imports import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = i == 0 or flowerbed[i-1] == 0
                empty_right = i == length-1 or flowerbed[i+1] == 0

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    result += 1
                    if result >= n:
                        return True
        
        return result >= n
