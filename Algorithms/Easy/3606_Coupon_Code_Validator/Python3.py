from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pattern = re.compile(r"^[A-Za-z0-9_]+$")
        business = set(["electronics", "grocery", "pharmacy", "restaurant"])

        result = []
        for c, b, a in zip(code, businessLine, isActive):
            if c and pattern.fullmatch(c) and b in business and a:
                result.append((b, c))

        return [c for _, c in sorted(result)]
