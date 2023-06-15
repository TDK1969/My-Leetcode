"""
日期: 2023-06-15
题目: 构建回文串检测
链接: https://leetcode-cn.com/problems/can-make-palindrome-from-substring/
"""

from typing import *
from collections import *
from string import ascii_lowercase
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ (1 << (ord(s[i]) - 97))
        
        res = []
        for l, r, k in queries:
            temp = pre[r + 1] ^ pre[l]
            cnt = 0
            while temp:
                cnt += temp & 1
                temp >>= 1
            res.append(cnt <= 2 * k + 1)
        return res
            

    

test = Solution()
print(test.canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))


        