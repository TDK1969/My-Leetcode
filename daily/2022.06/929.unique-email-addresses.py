"""
日期: 2022-06-04
题目: 独特的电子邮件地址
链接: https://leetcode-cn.com/problems/unique-email-addresses/
"""

from typing import *
from collections import *
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            (local_name, domain_name) = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            ans.add(local_name + "@" + domain_name)
        return len(ans)

test = Solution()
print(test.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))