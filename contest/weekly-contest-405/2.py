
from typing import *
from collections import *
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        tmp = []
        def dfs(l: int):
            if l == n:
                ans.append("".join(tmp))
                return
            else:
                if l == 0:
                    tmp.append("1")
                    dfs(l + 1)
                    tmp.pop()

                    tmp.append("0")
                    dfs(l + 1)
                    tmp.pop()
                else:
                    if tmp[-1] == "0":
                        tmp.append("1")
                        dfs(l + 1)
                        tmp.pop()
                    else:
                        tmp.append("1")
                        dfs(l + 1)
                        tmp.pop()

                        tmp.append("0")
                        dfs(l + 1)
                        tmp.pop()


        dfs(0)
        return ans


print(Solution().validStrings(3))
