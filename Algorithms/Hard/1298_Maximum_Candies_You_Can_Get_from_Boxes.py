from imports import *

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque()
        have_boxes = set()
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                have_boxes.add(box)

        collected_candies = 0
        while queue:
            box = queue.popleft()
            collected_candies += candies[box]
            
            for key in keys[box]:
                status[key] = 1

            for boxes in containedBoxes[box]:
                if status[boxes] == 1:
                    queue.append(boxes)
                else:
                    have_boxes.add(boxes)
            
            new = set()
            for box in have_boxes:
                if status[box] == 1:
                    queue.append(box)
                    new.add(box)
            
            for n in new:
                have_boxes.remove(n)
        
        return collected_candies
