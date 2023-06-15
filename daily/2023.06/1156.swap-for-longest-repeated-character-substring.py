"""
日期: 2023-06-03
题目: 单字符重复子串的最大长度
链接: https://leetcode-cn.com/problems/swap-for-longest-repeated-character-substring/
"""

from typing import *
from collections import *
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        c = Counter(text)
        i = j = k = 0
        ans = 1

        while i < n:
            j = i
            while j < n and text[i] == text[j]:
                j += 1
            # text[i:j]是长度为j - i的重复子串
            l1 = j - i
            k = j + 1

            while k < n and text[i] == text[k]:
                k += 1
            
            # text[j + 1:k]是长度为k - j - 1的重复子串
            l2 = k - j - 1

            ans = max(ans, min(c[text[i]], l1 + l2 + 1))

            # l1 + l2 + 1中的+1是精髓
            # 为了处理"acbaaa"这种例子,即在处理后三个a时,需要将前面的b换成a.
            # 此时因为后三个a已经到达字符串结尾,因此l2 = 0,但仍然进行+1,即前面可替换
            i = j
        return ans


test = Solution()
print(test.maxRepOpt1("acbaaa"))

