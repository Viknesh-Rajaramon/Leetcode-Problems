class Solution:
    def longestBalanced(self, s: str) -> int:
        n, count_0 = len(s), s.count("0")
        count_1 = n - count_0
        if count_0 == count_1:
            return n

        max_limit = 2*min(count_0, count_1)
        if max_limit == 0:
            return 0
        
        result, first_pos, second_pos, prefix_sum = 0, {0: -1}, {}, 0
        for i, c in enumerate(s):
            prefix_sum += (3 if c == '1' else 1)
            if prefix_sum in first_pos:
                if i-first_pos[prefix_sum] <= max_limit:
                    result = max(result, i - first_pos[prefix_sum])
                elif prefix_sum in second_pos:
                    result = max(result, i - second_pos[prefix_sum])
            
            prefix_sum -= 4
            if prefix_sum in first_pos:
                if i-first_pos[prefix_sum] <= max_limit:
                    result = max(result, i - first_pos[prefix_sum])
                elif (prefix_sum in second_pos):
                    result = max(result, i - second_pos[prefix_sum])

            prefix_sum += 2
            if prefix_sum not in first_pos:
                first_pos[prefix_sum] = i
            else:
                result = max(result, i - first_pos[prefix_sum])

                if prefix_sum not in second_pos:
                    second_pos[prefix_sum] = i
        
        return result
