class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid
        
        left_sum, right_sum = sum(nums[ : low+1]), sum(nums[low : ])
        if left_sum == right_sum:
            return -1
        
        return 0 if left_sum > right_sum else 1
