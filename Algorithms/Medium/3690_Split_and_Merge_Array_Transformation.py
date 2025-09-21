from imports import *

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return 0
        
        n = len(nums1)
        nums1, nums2 = tuple(nums1), tuple(nums2)
        seen = set([nums1])
        
        q = deque([(nums1, 0)])
        while q:
            arr, ops = q.popleft()

            for l in range(n):
                for r in range(n):
                    sub = arr[l : r+1]
                    rest = arr[ : l] + arr[r+1 : ]

                    for i in range(len(rest) + 1):
                        new_arr = tuple(rest[ : i] + sub + rest[i :])
                        if new_arr == nums2:
                            return ops + 1
            
                        if new_arr not in seen:
                            seen.add(new_arr)
                            q.append((new_arr, ops+1))

        return -1
