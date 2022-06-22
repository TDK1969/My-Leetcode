"""
日期: 2022-06-21
题目: IP 地址无效化
链接: https://leetcode-cn.com/problems/defanging-an-ip-address/
"""

from typing import *
from collections import *
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")