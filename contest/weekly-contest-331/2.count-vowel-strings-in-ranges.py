"""
题目: 统计范围内的元音字符串数
链接: https://leetcode-cn.com/problems/count-vowel-strings-in-ranges/
"""

from typing import *
from collections import *
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        yuan = set(["a", "e", "i", "o", "u"])
        cnt = [0 for _ in range(n + 1)]
        i = 1
        for word in words:
            if word[0] in yuan and word[-1] in yuan:
                cnt[i] += 1
            cnt[i] += cnt[i - 1]
            i += 1

        ans = []
        for s, e in queries:
            ans.append(cnt[e + 1] - cnt[s])
        return ans

test = Solution()
print(test.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))

        
