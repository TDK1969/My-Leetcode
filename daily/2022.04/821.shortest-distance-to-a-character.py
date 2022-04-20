"""
日期: 2022-04-19
题目: 字符的最短距离
链接: https://leetcode-cn.com/problems/shortest-distance-to-a-character/
"""
from typing import List
from collections import deque

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float("inf") for _ in range(n)]
        if s[0] == c:
            ans[0] = 0
        if s[-1] == c:
            ans[-1] = 0

        for i in range(1, n):
            if s[i] == c:
                ans[i] = 0
            else:
                ans[i] = ans[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            ans[i] = min(ans[i], ans[i + 1] + 1)

        return ans

test = Solution()
print(test.shortestToChar("loveleetcode", "e"))

        
