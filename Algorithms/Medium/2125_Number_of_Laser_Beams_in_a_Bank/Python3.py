from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result, prev_count = 0, 0
        for lasers in bank:
            curr_count = lasers.count("1")
            if not curr_count:
                continue
            
            result += prev_count * curr_count
            prev_count = curr_count
        
        return result
