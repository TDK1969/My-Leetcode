"""
日期: 2022-07-07
题目: 单词替换
链接: https://leetcode-cn.com/problems/replace-words/
"""

from typing import *
from collections import *

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_dict = {}
        for word in dictionary:
            t = root_dict
            for alpha in word:
                if alpha not in t:
                    t[alpha] = {}
                t = t[alpha]
            t['is_word'] = {}
        
        ans = []
        for word in sentence.split():
            t = root_dict
            flag = True
            for i, alpha in enumerate(word):
                if "is_word" not in t:
                    if alpha not in t:
                        break
                    t = t[alpha]
                else:
                    ans.append(word[:i])
                    flag = False
                    break
            if flag:
                ans.append(word)
        
        return " ".join(ans)

test = Solution()
print(test.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))


        


        