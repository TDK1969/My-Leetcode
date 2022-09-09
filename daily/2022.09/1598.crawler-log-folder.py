"""
日期: 2022-09-09
题目: 文件夹操作日志搜集器
链接: https://leetcode-cn.com/problems/crawler-log-folder/
"""

from typing import *
from collections import *
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "../":
                if ans > 0:
                    ans -= 1
            elif log == "./":
                pass
            else:
                ans += 1
        return ans