"""
日期: 2024-11-18
题目: 图片平滑器
链接: https://leetcode.cn/problems/image-smoother/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                cnt = 0
                s = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= x + dx < m and 0 <= y + dy < n:
                            cnt += 1
                            s += img[x + dx][y + dy]
                ans[x][y] = s // cnt
        return ans
print(Solution().imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))


"""
--TESTCASE BEGIN--
TestCase 0: [[1,1,1],[1,0,1],[1,1,1]]
TestCase 1: [[100,200,100],[200,50,200],[100,200,100]]
--TESTCASE END--
""" 
