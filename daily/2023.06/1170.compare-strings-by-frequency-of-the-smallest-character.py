"""
日期: 2023-06-10
题目: 比较字符串最小字母出现频次
链接: https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character/
"""

from typing import *
from collections import *
import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def calc(word: str) -> int:
            return word.count(min(word))

        words_cnt = [calc(word) for word in words]
        words_cnt.sort()

        ans = []

        for query in queries:
            l = bisect.bisect_right(words_cnt, calc(query))
            ans.append(len(words) - l)
        return ans

test = Solution()
print(test.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"]))