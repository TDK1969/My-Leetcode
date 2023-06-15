"""
日期: 2023-02-21
题目: 灌溉花园的最少水龙头数目
链接: https://leetcode-cn.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
"""

from typing import *
from collections import *
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        covers = []
        for i, r in enumerate(ranges):
            covers.append((max(0, i - r), min(n, i + r)))
        
        covers.sort(key=lambda x:(x[0], -x[1]))

        i = j = 0
        cnt = 1
        cur_left, cur_right = covers[0]
        if cur_left != 0:
            return -1
        if cur_right == n:
            return 1
        
        while 1:
            j = i + 1
            k = -1
            nxt_right = -1
            while j <= n and covers[j][0] <= cur_right:
                if covers[j][1] > cur_right and covers[j][1] > nxt_right:
                    nxt_right = max(nxt_right, covers[j][1])
                j += 1
            if nxt_right == -1:
                return -1

            i = j
            cur_right = nxt_right
            cnt += 1

            if nxt_right == n:
                break
            
        
        return cnt

t = Solution()
print(t.minTaps(n = 35, ranges = [1,0,4,0,4,1,4,3,1,1,1,2,1,4,0,3,0,3,0,3,0,5,3,0,0,1,2,1,2,4,3,0,1,0,5,2]))


            
