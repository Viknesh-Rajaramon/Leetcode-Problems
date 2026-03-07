class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        result, freq_1, freq_2, left_1, left_2, distinct, enough = 0, {}, {}, 0, 0, 0, 0
        for num in nums:
            if num not in freq_1:
                freq_1[num] = 0
                distinct += 1
            
            if num not in freq_2:
                freq_2[num] = 0
            
            freq_1[num] += 1
            freq_2[num] += 1
            if freq_2[num] == m:
                enough += 1
            
            while distinct > k:
                freq_1[nums[left_1]] -= 1
                if freq_1[nums[left_1]] == 0:
                    del freq_1[nums[left_1]]
                    distinct -= 1
                
                left_1 += 1
            
            while enough >= k:
                if freq_2[nums[left_2]] == m:
                    enough -= 1
                
                freq_2[nums[left_2]] -= 1
                if freq_2[nums[left_2]] == 0:
                    del freq_2[nums[left_2]]
                
                left_2 += 1
            
            result += max(0, left_2 - left_1)
        
        return result
