"""
日期: 2023-02-08
题目: 删除子文件夹
链接: https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/
"""

from typing import *
from collections import *
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        pre = "//"
        for f in folder:
            if not f.startswith(pre):
                ans.append(f)
                pre = f + "/"
        return ans

test = Solution()
print(test.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))

