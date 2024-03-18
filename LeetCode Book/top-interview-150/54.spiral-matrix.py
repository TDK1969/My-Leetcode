"""
日期: 2022-07-14
题目: 螺旋矩阵
链接: https://leetcode-cn.com/problems/spiral-matrix/
"""

from typing import *
from collections import *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        turning_point = [[0, n - 1], [m - 1, n - 1], [m - 1, 0], [1, 0]]
        point_change = [[1, -1], [-1, -1], [-1, 1], [1, 1]]
        p = 0
        i = j = 0

        for _ in range(m * n):
            if i == turning_point[p][0] and j == turning_point[p][1]:
                turning_point[p][0] += point_change[p][0]
                turning_point[p][1] += point_change[p][1]
                p = (p + 1) % 4
            ans.append(matrix[i][j])
            i += dirs[p][0]
            j += dirs[p][1]
        
        return ans
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        # 初始化上下左右 四条边界
        top, bottom, left, right = 0, m - 1, 0, n - 1

        # 外层循环,每次输出一圈
        while True:
            # 输出上边
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            # 若上边界越过边界,则退出
            if top > bottom:
                break
            
            # 输出右边
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            # 若右边界越过左边界,则退出
            if right < left:
                break
            
            # 输出下边
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            # 若下边界越过上边界,则退出
            if bottom < top:
                break
            
            # 输出左边
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            # 若右边界越过左边界,则退出
            if right < left:
                break
        return ans

test = Solution()
print(test.spiralOrder([[1,2,3,4]]))
            

        


