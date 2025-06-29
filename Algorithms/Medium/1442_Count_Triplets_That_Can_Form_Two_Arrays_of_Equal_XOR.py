from imports import *

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        
        prefix_xor = [0]
        for i in range(n):
            prefix_xor.append(prefix_xor[-1] ^ arr[i])
        
        result = 0
        for i in range(2, n+1):
            for j in range(i):
                if prefix_xor[i] ^ prefix_xor[j] == 0:
                    result += i-j-1
        
        return result
