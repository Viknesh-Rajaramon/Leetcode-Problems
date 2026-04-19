from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0

        fruit_1, fruit_2 = -1, -1
        count_1, count_2, prev = 0, 0, 0

        for f in fruits:
            if f == fruit_1:
                count_1 += 1
                prev += 1
            elif f == fruit_2:
                fruit_1, fruit_2 = fruit_2, fruit_1
                count_1, count_2, prev = count_2 + 1, count_1, 1
            else:
                result = max(result, count_1 + count_2)
                fruit_1, fruit_2 = f, fruit_1
                count_1, count_2, prev = 1, prev, 1

        return max(result, count_1 + count_2)
