"""
题目: 完成所有任务需要的最少轮数
链接: https://leetcode-cn.com/problems/minimum-rounds-to-complete-all-tasks/
"""
from typing import List
from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ans = 0
        for _, times in counter.most_common():
            if times % 3 == 0:
                ans += times // 3
            elif times == 1:
                return -1
            else:
                ans += times // 3 + 1
        return ans