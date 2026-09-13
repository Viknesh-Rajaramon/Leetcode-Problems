from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n, img1_points, img2_points, d = len(img1), [], [], {}
        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    img1_points.append((r, c))
                
                if img2[r][c]:
                    img2_points.append((r, c))
        
        for ra, ca in img1_points:
            for rb, cb in img2_points:
                key = (rb - ra, cb - ca)
                if key not in d:
                    d[key] = 0

                d[key] += 1
        
        result = 0
        for val in d.values():
            result = max(result, val)

        return result
