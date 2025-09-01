from imports import *

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        result = []
        for o in order:
            if o in friends:
                result.append(o)
        
        return result
