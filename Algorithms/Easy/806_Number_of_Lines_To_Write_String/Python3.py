from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ord_a = ord("a")
        line, curr_width = 1, 0
        for c in s:
            width = widths[ord(c) - ord_a]
            if curr_width + width > 100:
                line += 1
                curr_width = width
            else:
                curr_width += width
        
        return [line, curr_width]
