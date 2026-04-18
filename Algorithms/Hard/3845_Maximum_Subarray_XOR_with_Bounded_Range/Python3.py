from collections import deque

class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        result, l, n, max_q, min_q = 0, 0, len(nums), deque(), deque()
        max_bit_len = max(num.bit_length() for num in nums)
        trie, pref = {1 << i: -1 for i in range(max_bit_len+2)}, 1 << (max_bit_len+1)
        for r in range(n):
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()

            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            
            max_q.append(r)
            min_q.append(r)

            while nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == l:
                    max_q.popleft()
                
                if min_q[0] == l:
                    min_q.popleft()

                l += 1
            
            pref ^= nums[r]
            for i in range(max_bit_len):
                trie[pref >> i] = r
            
            pref_left = 1
            for i in range(max_bit_len, -1, -1):
                pref_left <<= 1
                mask = (pref >> i) & 1
                max_xor = pref_left | mask ^ 1
                if trie.get(max_xor, -2) >= l-1:
                    pref_left = max_xor
                else:
                    pref_left |= mask
                
            result = max(result, pref_left ^ pref)
        
        return result
