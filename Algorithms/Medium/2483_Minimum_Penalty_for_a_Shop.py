class Solution:
    def bestClosingTime(self, customers: str) -> int:
        result, min_pen, count = -1, 0, 0
        for i, c in enumerate(customers):
            if c == "Y":
                count += 1
            else:
                count -= 1
            
            if count > min_pen:
                result, min_pen = i, count

        return result+1
