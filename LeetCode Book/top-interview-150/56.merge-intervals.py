"""
日期: 2022-07-14
题目: 合并区间
链接: https://leetcode-cn.com/problems/merge-intervals/
"""

from typing import *
from collections import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 对原数组排序,能够合并的区间一定是连续的
        intervals.sort()
        n = len(intervals)
        ans = []
        i = j = 0

        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            j = i
            while j < n:
                # 如果与intervals[i]有交集,则更新right
                if intervals[j][0] <= right:
                    right = max(right, intervals[j][1])
                else:
                    break
                j += 1
            ans.append([left, right])
            i = j
        
        return ans


test = Solution()
print(test.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
        
