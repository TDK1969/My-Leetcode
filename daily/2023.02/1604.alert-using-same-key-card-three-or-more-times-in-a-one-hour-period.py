"""
日期: 2023-02-07
题目: 警告一小时内使用相同员工卡大于等于三次的人
链接: https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
"""

from typing import *
from collections import *
import heapq
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        n = len(keyName)
        for i in range(n):
            t = int(keyTime[i][:2]) * 60 + int(keyTime[i][3:5])
            d[keyName[i]].append(t)
        
        ans = []
        
        for name in d:
            d[name].sort()
            for i in range(2, len(d[name])):
                if d[name][i] - d[name][i - 2] <= 60:
                    ans.append(name)
                    break
            
        ans.sort()
        return ans
