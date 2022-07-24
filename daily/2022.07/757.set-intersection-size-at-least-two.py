"""
日期: 2022-07-22
题目: 设置交集大小至少为2
链接: https://leetcode-cn.com/problems/set-intersection-size-at-least-two/
"""

from typing import *
from collections import *
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, n, m = 0, len(intervals), 2
        vals = [[] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            j = intervals[i][0]
            for k in range(len(vals[i]), m):
                ans += 1
                for p in range(i - 1, -1, -1):
                    if intervals[p][1] < j:
                        break
                    vals[p].append(j)
                j += 1
        return ans
test = Solution()
print(test.intersectionSizeTwo([[4,7],[5,8],[7,9],[2,6],[0,1],[1,4],[1,9],[0,5],[5,10],[7,8]]))

