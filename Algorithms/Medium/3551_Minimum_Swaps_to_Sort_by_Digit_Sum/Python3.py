from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_of_digits(num: int) -> int:
            result = 0
            while num > 0:
                result += num % 10
                num //= 10
                
            return result

        result, n, sorted_nums = 0, len(nums), sorted(nums, key = lambda x: (sum_of_digits(x), x))
        val_idx_map, visited = {val: idx for idx, val in enumerate(sorted_nums)}, [False] * n
        for i in range(n):
            if visited[i] or val_idx_map[nums[i]] == i:
                continue

            cycle_size, j = 0, i
            while not visited[j]:
                visited[j] = True
                j = val_idx_map[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                result += cycle_size - 1

        return result
