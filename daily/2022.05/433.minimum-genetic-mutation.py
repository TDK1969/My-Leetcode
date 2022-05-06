"""
日期: 2022-05-07
题目: 最小基因变化
链接: https://leetcode-cn.com/problems/minimum-genetic-mutation/
"""

from typing import *
from collections import *


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque()
        bank = set(bank)
        visited = set(start)
        gene = ["A", "C", "G", "T"]

        queue.append((start, 0))

        while queue:
            cur, turn = queue.popleft()
            if cur == end:
                return turn
            else:
                for i in range(8):
                    for g in gene:
                        temp = cur[:i] + g + cur[i + 1:]
                        if temp not in visited and temp in bank:
                            queue.append((temp, turn + 1))
                            visited.add(temp)
        return -1

test = Solution()
print(test.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
