class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        result, n = 0, len(nums)
        def check_rotate_sorted(nums: list[int]) -> bool:
            n, downs, down_val, min_val = len(nums), 0, 0, nums[0]
            for i in range(n):
                min_val = min(min_val, nums[i])
                if nums[(i+1) % n] < nums[i]:
                    downs += 1
                    down_val = nums[(i+1) % n]
            
            if (downs == 0) or (downs == 1 and down_val == min_val):
                return True
            
            return False
        
        def k_partition(nums: list[int], k: int) -> list[list[int]]:
            res = []
            for i in range(0, n, k):
                res.append(nums[i : i+k])
            
            return res

        for k in range(1, n+1):
            if n%k != 0:
                continue

            partitions = k_partition(nums, k)
            n_p, sortable = len(partitions), True
            for i in range(n_p):
                if not check_rotate_sorted(partitions[i]):
                    sortable = False
                    break
                
                if i+1 < n_p and max(partitions[i]) > min(partitions[i+1]):
                    sortable = False
                    break
            
            if sortable:
                result += k
        
        return result
