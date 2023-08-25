"""
日期: 2023-08-24
题目: 统计参与通信的服务器
链接: https://leetcode-cn.com/problems/count-servers-that-communicate/
"""

from typing import *
from collections import *
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        servers = []
        m, n = [0 for _ in range(len(grid))], [0 for _ in range(len(grid[0]))]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    servers.append((x, y))
                    m[x] += 1
                    n[y] += 1
        
        for x, y in servers:
            if m[x] == 1 and n[y] == 1:
                ans += 1
        
        return len(servers) - ans
                
