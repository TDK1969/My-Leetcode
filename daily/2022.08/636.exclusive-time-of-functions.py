"""
日期: 2022-08-07
题目: 函数的独占时间
链接: https://leetcode-cn.com/problems/exclusive-time-of-functions/
"""

from typing import *
from collections import *
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        log = []
        for l in logs:
            temp_l = l.split(":")
            log.append((int(temp_l[0]), temp_l[1], int(temp_l[2])))
        log.sort(key=lambda x:x[2])

        stack = []
        ans  = [0 for _ in range(n)]

        for idx, s, t in log:
            if s == "start":
                if stack:
                    ans[stack[-1][0]] += t - stack[-1][1]
                stack.append([idx, t])
            elif s == "end":
                ans[idx] += t - stack[-1][1] + 1
                stack.pop()
                if stack:
                    stack[-1][1] = t + 1
        return ans

test = Solution()
print(test.exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
                    


