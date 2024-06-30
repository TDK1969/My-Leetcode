"""
日期: 2024-04-07
题目: 王位继承顺序
链接: https://leetcode.cn/problems/throne-inheritance/
"""

from typing import *
from collections import *
from leetcode_utils import *
class ThroneInheritance:

    def __init__(self, kingName: str):


    def birth(self, parentName: str, childName: str) -> None:


    def death(self, name: str) -> None:


    def getInheritanceOrder(self) -> List[str]:



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

"""
--TESTCASE BEGIN--
TestCase 0: ["ThroneInheritance","birth","birth","birth","birth","birth","birth","getInheritanceOrder","death","getInheritanceOrder"],[["king"],["king","andy"],["king","bob"],["king","catherine"],["andy","matthew"],["bob","alex"],["bob","asha"],[None],["bob"],[None]]
--TESTCASE END--
""" 
