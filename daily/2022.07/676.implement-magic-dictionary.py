"""
日期: 2022-07-11
题目: 实现一个魔法字典
链接: https://leetcode-cn.com/problems/implement-magic-dictionary/
"""

from typing import *
from collections import *
class MagicDictionary:

    def __init__(self):
        self.root = dict()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            t = self.root
            for ch in word:
                if ch not in t:
                    t[ch] = dict()
                t = t[ch]
            t['is_word'] = True


    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        def dfs(t: Dict, pos: int, change: bool) -> bool:
            if pos == n:
                return 'is_word' in t and change
            else:
                ch = searchWord[pos]
                if change:
                    if ch in t:
                        return dfs(t[ch], pos + 1, change)
                    else:
                        return False
                elif not change:
                    for nxt in t.keys():
                        if nxt != "is_word":
                            if dfs(t[nxt], pos + 1, nxt != ch):
                                return True

                return False
        return dfs(self.root, 0, False)
            

test = MagicDictionary()
test.buildDict(["hello", "leetcode", "hallo"])
print(test.search("hello"))
print(test.search("hellx"))




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)