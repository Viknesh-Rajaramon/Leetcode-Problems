from math import ceil

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        result, cubes, first = set(), [num**3 for num in range(1, ceil(n**(1/3)))], set()
        for i, a_3 in enumerate(cubes):
            for b_3 in cubes[i : ]:
                cube = a_3 + b_3
                if cube > n:
                    break
                
                if cube not in first:
                    first.add(cube)
                else:
                    result.add(cube)

        return sorted(result)
