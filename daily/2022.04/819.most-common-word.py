"""
日期: 2022-04-17
题目: 最常见的单词
链接: https://leetcode-cn.com/problems/most-common-word/
"""
from typing import List
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        s = {'!', '?', "'", ',', ';', '.', ' '}
        p = ""
        words = []
        for value in paragraph:
            if value in s:
                if p:
                    words.append(p)
                p = ""
            else:
                p += value
        if p:
            words.append(p)
    
        counter = defaultdict(int)
        for word in words:
            w = word.lower()
            if w not in banned:
                counter[w] += 1
        maxCount = 0
        ans = ""
        for word, count in counter.items():
            if count > maxCount:
                ans = word
                maxCount = count
        
        return ans

test = Solution()
print(test.mostCommonWord("Bob", []))
