"""
日期: 2023-11-09
题目: 逃离火灾
链接: https://leetcode-cn.com/problems/escape-the-spreading-fire/
"""

from typing import *
from collections import *
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 返回三个数，分别表示到达安全屋/安全屋左边/安全屋上边的最短时间
        def bfs(q: List[Tuple[int, int]]) -> (int, int, int):
            time = [[-1] * n for _ in range(m)]  # -1 表示未访问
            for i, j in q:
                time[i][j] = 0
            t = 1
            while q:  # 每次循环向外扩展一圈
                tmp = q
                q = []
                for i, j in tmp:
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and time[x][y] < 0:
                            time[x][y] = t
                            q.append((x, y))
                t += 1
            return time[-1][-1], time[-1][-2], time[-2][-1]

        man_to_house_time, m1, m2 = bfs([(0, 0)])
        if man_to_house_time < 0:  # 人无法到安全屋
            return -1

        fire_pos = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 1]
        fire_to_house_time, f1, f2 = bfs(fire_pos)
        if fire_to_house_time < 0:  # 火无法到安全屋
            return 10 ** 9

        d = fire_to_house_time - man_to_house_time
        if d < 0:  # 火比人先到安全屋
            return -1

        if m1 != -1 and m1 + d < f1 or \
           m2 != -1 and m2 + d < f2:  # 安全屋左边或上边的其中一个格子人比火先到
            return d  # 图中第一种情况
        return d - 1  # 图中第二种情况
