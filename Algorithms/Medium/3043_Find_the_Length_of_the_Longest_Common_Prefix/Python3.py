from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            while num > 0:
                if num in prefixes:
                    break
                
                prefixes.add(num)
                num //= 10
        
        result = 0
        for num in arr2:
            while num > result:
                if num in prefixes:
                    result = num
                    break
                
                num //= 10

        return len(str(result)) if result else 0
