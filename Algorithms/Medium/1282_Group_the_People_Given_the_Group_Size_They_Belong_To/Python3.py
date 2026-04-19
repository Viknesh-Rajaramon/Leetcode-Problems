from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)

        result = []
        for id_, size in enumerate(groupSizes):
            groups[size].append(id_)

            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []
        
        return result
