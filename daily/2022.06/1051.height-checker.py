"""
日期: 2022-06-13
题目: 高度检查器
链接: https://leetcode-cn.com/problems/height-checker/
"""

from typing import *
from collections import *
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        k = max(heights)
        cnt = [0 for _ in range(k + 1)]
        for i in heights:
            cnt[i] += 1
        idx = 0
        for i in range(k + 1):
            while cnt[i]:
                if i != heights[idx]:
                    ans += 1
                cnt[i] -= 1
                idx += 1
        
        return ans

test = Solution()
print(test.heightChecker([1,1,4,2,1,3]))
