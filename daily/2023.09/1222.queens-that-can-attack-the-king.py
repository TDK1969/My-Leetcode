"""
日期: 2023-09-14
题目: 可以攻击国王的皇后
链接: https://leetcode-cn.com/problems/queens-that-can-attack-the-king/
"""

from typing import *
from collections import *
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kx, ky = king[0], king[1]
        ans = [False] * 8
        q = [[0, 0] for _ in range(8)]
        for qx, qy in queens:
            if kx == qx and ky < qy:
                if not ans[0] or qy < q[0][1]:
                    q[0][0], q[0][1] = qx, qy
                ans[0] = True
            if kx == qx and ky > qy:
                if not ans[1] or qy > q[1][1]:
                    q[1][0], q[1][1] = qx, qy
                ans[1] = True
            if ky == qy and kx < qx:
                if not ans[2] or qx < q[2][0]:
                    q[2][0], q[2][1] = qx, qy
                ans[2] = True
            if ky == qy and kx > qx:
                if not ans[3] or qx > q[3][0]:
                    q[3][0], q[3][1] = qx, qy
                ans[3] = True
            if kx + ky == qx + qy:
                if kx < qx:
                    if not ans[4] or qx < q[4][0]:
                        q[4][0], q[4][1] = qx, qy
                    ans[4] = True
                else:
                    if not ans[5] or qx > q[5][0]:
                        q[5][0], q[5][1] = qx, qy
                    ans[5] = True
            if kx - ky == qx - qy:
                if kx < qx:
                    if not ans[6] or qx < q[6][0]:
                        q[6][0], q[6][1] = qx, qy
                    ans[6] = True
                else:
                    if not ans[7] or qx > q[7][0]:
                        q[7][0], q[7][1] = qx, qy
                    ans[7] = True
        return [q[i] for i in range(8) if ans[i]]
        
    

test = Solution()
print(test.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))