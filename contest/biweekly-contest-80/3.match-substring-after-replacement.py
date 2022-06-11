"""
题目: 替换字符后匹配
链接: https://leetcode-cn.com/problems/match-substring-after-replacement/
"""

from typing import *
from collections import *

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if sub in s:
            return True

        s_set = set(s)
        sub_set = set(sub)
        m = defaultdict(set)

        for old, new in mappings:
            if old in sub_set and new in s_set:
                m[old].add(new)
        
        n = len(s)
        k = len(sub)
        for i in range(n):
            if i + k > n:
                break
            temp = s[i:i + k]
            flag = True
            for j in range(k):
                if temp[j] != sub[j] and temp[j] not in m[sub[j]]:
                    flag = False
                    break
            if flag:
                return True

        return False 

test = Solution()
print(test.matchReplacement(s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]))
            

        


                
        

            