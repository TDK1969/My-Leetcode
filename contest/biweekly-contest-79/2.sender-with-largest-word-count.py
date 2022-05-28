"""
题目: 最多单词数的发件人
链接: https://leetcode-cn.com/problems/sender-with-largest-word-count/
"""

from typing import *
from collections import *

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        n = len(messages)

        for i in range(n):
            d[senders[i]] += len(messages[i].split())
        
        temp = list(d.items())
        temp.sort(key=lambda x:[x[1], x[0]])
        return temp[-1][0]


test = Solution()
print(test.largestWordCount(messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]))