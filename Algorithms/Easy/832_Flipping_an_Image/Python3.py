from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            j = 0
            while j < n //2:
                image[i][j], image[i][n-1-j] = (image[i][n-1-j]+1) % 2, (image[i][j]+1) % 2
                j += 1

            if n % 2:
                image[i][n//2] = (image[i][n//2]+1) % 2

        return image
