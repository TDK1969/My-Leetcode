"""
题目: 道路的最大总重要性
链接: https://leetcode-cn.com/problems/maximum-total-importance-of-roads/
"""

from typing import *
from collections import *

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for s, e in roads:
            cnt[s] += 1
            cnt[e] += 1
        temp = list(cnt.values())
        temp.sort(reverse=True)
        ans = 0
        k = n
        for value in temp:
            ans += k * value
            k -= 1

        return ans

test = Solution()
print(test.maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))