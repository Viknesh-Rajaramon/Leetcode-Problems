from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        result = 0
        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            
            number_of_boxes = min(truckSize, boxes)
            result += number_of_boxes * units
            truckSize -= number_of_boxes
        
        return result
