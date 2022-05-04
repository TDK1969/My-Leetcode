"""
日期: 2022-05-03
题目: 重新排列日志文件
链接: https://leetcode-cn.com/problems/reorder-data-in-log-files/
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_log = []
        digit_log = []

        for log in logs:
            t = log.split()
            mark = t[0]
            content = " ".join(t[1:])

            if t[1].isalpha():
                alpha_log.append(log)
            else:
                digit_log.append(log)
        
        alpha_log.sort(key=lambda x:(" ".join(x.split()[1:]), x.split()[0]))
        return alpha_log + digit_log

test = Solution()
print(test.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))