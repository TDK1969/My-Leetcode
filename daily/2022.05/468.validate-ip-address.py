"""
日期: 2022-05-29
题目: 验证IP地址
链接: https://leetcode-cn.com/problems/validate-ip-address/
"""

from typing import *
from collections import *
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        n = len(queryIP)
        if "." in queryIP and 7 <= n <= 15:
            nums = queryIP.split(".")
            if len(nums) != 4:
                return "Neither"
            for num in nums:
                if len(num) > 3 or not num.isdigit() or not (0 <= int(num) <= 255) or str(int(num)) != num:
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP and 15 <= n <= 39:
            valid_IPv6 = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}
            nums = queryIP.split(":")
            if len(nums) != 8:
                return "Neither"
            for num in nums:
                if 0 < len(num) <= 4:
                    for i in num:
                        if i not in valid_IPv6:
                            return "Neither"
                else:
                    return "Neither"
            return "IPv6"

        else:
            return "Neither"

test = Solution()
print(test.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))