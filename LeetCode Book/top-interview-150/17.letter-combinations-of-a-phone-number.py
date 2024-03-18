"""
日期: 2022-07-14
题目: 电话号码的字母组合
链接: https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import *
from collections import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []
        cnt = ""
        if not digits:
            return ans
        def dfs(i: int):
            nonlocal cnt
            if i == len(digits):
                ans.append(cnt[:])
                return
            for alphas in d[digits[i]]:
                for alpha in alphas:
                    cnt += alpha
                    dfs(i + 1)
                    cnt = cnt[:-1]
        dfs(0)
        return ans

test = Solution()
print(test.letterCombinations("23"))
                    
                    


