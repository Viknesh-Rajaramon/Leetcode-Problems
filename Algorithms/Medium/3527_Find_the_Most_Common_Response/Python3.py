from typing import List
from collections import defaultdict

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        n = len(responses)
        
        common_responses = defaultdict(int)
        for i in range(n):
            for r in set(responses[i]):
                common_responses[r] += 1
        
        common_responses = sorted(common_responses.items(), key = lambda x: (-x[1], x[0]))
        return common_responses[0][0]
