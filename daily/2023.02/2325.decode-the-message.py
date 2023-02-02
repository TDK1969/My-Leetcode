"""
日期: 2023-02-01
题目: 解密消息
链接: https://leetcode-cn.com/problems/decode-the-message/
"""

from typing import *
from collections import *
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        cnt = 0
        for k in key:
            if k != " " and k not in d:
                d[k] = cnt
                cnt += 1
        
        ans = list(message)
        for i, k in enumerate(ans):
            if k in d:
                ans[i] = chr(97) + d[k]
        
        return "".join(ans)

test = Solution()
print(test.decodeMessage(key, message))




        