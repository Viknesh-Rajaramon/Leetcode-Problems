from imports import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        
        for j in range(1, n-1):
            left = []
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    left.append(arr[i])
            
            right = []
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    right.append(arr[k])
            
            right.sort()
            for num in left:
                l, r = 0, len(right)
                while l < r:
                    mid = (l+r) // 2
                    if right[mid] < num - c:
                        l = mid+1
                    else:
                        r = mid
                
                left_index = l

                l, r = 0, len(right)
                while l < r:
                    mid = (l+r) // 2
                    if right[mid] <= num + c:
                        l = mid+1
                    else:
                        r = mid
                
                right_index = l

                count += (right_index - left_index)
        
        return count
