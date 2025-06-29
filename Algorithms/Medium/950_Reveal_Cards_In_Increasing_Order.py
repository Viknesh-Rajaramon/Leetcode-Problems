from imports import *

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        result = [0] * n
        queue = deque(range(n))

        for i in range(n):
            result[queue.popleft()] = deck[i]
            if queue:
                queue.append(queue.popleft())

        return result
