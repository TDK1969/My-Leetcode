"""
日期: 2024-08-26
题目: 员工的重要性
链接: https://leetcode.cn/problems/employee-importance/
"""

from typing import *
from collections import *
from leetcode_utils import *
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        

"""
--TESTCASE BEGIN--
TestCase 0: [[1,5,[2,3]],[2,3,[]],[3,3,[]]],1
TestCase 1: [[1,2,[5]],[5,-3,[]]],5
--TESTCASE END--
""" 
