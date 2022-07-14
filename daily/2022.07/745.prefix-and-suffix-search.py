"""
日期: 2022-07-14
题目: 前缀和后缀搜索
链接: https://leetcode-cn.com/problems/prefix-and-suffix-search/
"""

from typing import *
from collections import *
class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_root = {}
        self.back_root = {}
        self.ans = {}

        for i, word in enumerate(words):
            t = self.pre_root
            for ch in word:
                if "#" not in t:
                    t['#'] = set()
                t['#'].add(i)

                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            if "#" not in t:
                t['#'] = set()
            t['#'].add(i)
            
            t = self.back_root
            for ch in word[::-1]:
                if "#" not in t:
                    t['#'] = set()
                t['#'].add(i)

                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            if "#" not in t:
                t['#'] = set()
            t['#'].add(i)

    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) in self.ans:
            return self.ans[(pref, suff)]
        t = self.pre_root
        for ch in pref:
            if ch in t:
                t = t[ch]
            else:
                return -1
        a = t['#']
        
        t = self.back_root
        for ch in suff[::-1]:
            if ch in t:
                t = t[ch]
            else:
                return -1
        b = t['#']

        c = a & b
        self.ans[(pref, suff)] = max(c) if c else -1
        return max(c) if c else -1
        

test = WordFilter(["apple"])
print(test.f("ap", "le"))



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)