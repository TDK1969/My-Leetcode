"""
日期: 2023-11-06
题目: 最大单词长度乘积
链接: https://leetcode-cn.com/problems/maximum-product-of-word-lengths/
"""

from typing import *
from collections import *

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        alpha_bit = defaultdict(int)
        for word in words:
            k = 0
            for alpha in word:
                k |= 1 << (ord(alpha) - ord('a'))
            alpha_bit[k] = max(alpha_bit[k], len(word))

        ans = 0
        t = list(alpha_bit.keys())
        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                if t[i] & t[j] == 0:
                    ans = max(ans, alpha_bit[t[i]] * alpha_bit[t[j]])
        
        return ans

print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
