from imports import *

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        group = defaultdict(list)
        for c, count in Counter(s).items():
            group[count].append(c)

        group = sorted(group.items(), key = lambda x: (len(x[1]), x[0]), reverse = True)
        return "".join(group[0][1])
