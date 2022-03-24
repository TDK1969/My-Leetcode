from typing import List
from math import floor
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                greySum = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n:
                            count += 1
                            greySum += img[x][y]
                ans[i][j] = floor(greySum / count)
        
        return ans
