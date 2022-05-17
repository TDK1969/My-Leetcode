"""
日期: 2022-05-17
题目: 验证外星语词典
链接: https://leetcode-cn.com/problems/verifying-an-alien-dictionary/
"""

from typing import *
from collections import *
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = {order[i]: i for i in range(len(order))}

        def cmp(s1: str, s2: str) -> bool:
            # return s1 < s2
            k = min(len(s1), len(s2))
            for i in range(k):
                if alien_order[s1[i]] > alien_order[s2[i]]:
                    return True
                elif alien_order[s1[i]] < alien_order[s2[i]]:
                    return False
            if len(s1) <= len(s2):
                return False
            else:
                return True
        
        for i in range(len(words) - 1):
            if cmp(words[i], words[i + 1]):
                return False
        
        #return words == sorted(words, key=lambda x: (alien_order[i] for i in x))
        return True

test = Solution()
print(test.isAlienSorted(words = ["word","world","row", "wor"], order = "worldabcefghijkmnpqstuvxyz"))