from imports import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {}
        n = len(nums2)
        
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            
            index_map[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        result = []
        for num in nums1:
            result.append(index_map[num])
        
        return result
