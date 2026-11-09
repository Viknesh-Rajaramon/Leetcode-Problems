class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n, ok = len(nums), True
        for i in range(n):
            if nums[i] != target[i]:
                ok = False
                break
        
        if ok:
            i = n-1
        
        nums[i : ] = sorted(nums[i : ], reverse = True)
        if nums != target:
            return 0
        
        result = 1
        for j in range(i-1, -1, -1):
            if target[j] < target[j+1]:
                break
            
            result += 1
        
        return result
