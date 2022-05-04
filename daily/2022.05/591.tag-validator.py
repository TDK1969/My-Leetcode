"""
日期: 2022-05-02
题目: 标签验证器
链接: https://leetcode-cn.com/problems/tag-validator/
"""
import re
class Solution:
    def isValid(self, code: str) -> bool:
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'

test = Solution()
print(test.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))