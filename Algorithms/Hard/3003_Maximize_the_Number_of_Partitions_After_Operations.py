from typing import List, Tuple

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        set_bits = [1 << (ord(c) - ord("a")) for c in s]
        def make_prefix(set_bits: List[int]) -> Tuple[List[int], List[int]]:
            prefix, prefix_mask = [0], [0]
            mask, group = 0, 0
            for curr_bit_set_index in set_bits:
                mask |= curr_bit_set_index
                if mask.bit_count() > k:
                    group += 1
                    mask = curr_bit_set_index
                
                prefix.append(group)
                prefix_mask.append(mask)
            
            return prefix, prefix_mask
        
        prefix, prefix_mask = make_prefix(set_bits)
        suffix, suffix_mask = make_prefix(set_bits[::-1])

        result = 0
        for i in range(len(s)):
            candidate = prefix[i] + suffix[-(i+2)] + 2
            mask = prefix_mask[i] | suffix_mask[-(i+2)]
            if prefix_mask[i].bit_count() == suffix_mask[-(i+2)].bit_count() == k and mask.bit_count() < 26:
                candidate += 1
            elif min(mask.bit_count() + 1, 26) <= k:
                candidate -= 1
            
            if candidate > result:
                result = candidate

        return result
