"""
日期: 2022-04-03
题目: 寻找比目标字母大的最小字母
链接: https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/
"""
from typing import List
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect.bisect(letters, target) % len(letters)]