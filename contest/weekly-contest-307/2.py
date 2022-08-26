from typing import *
from collections import *

class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        c = c.most_common()
        c = [list(i) for i in c]
        c.sort(key=lambda x:x[0], reverse=True)

        ans = ""
        for i in range(len(c)):
            key = c[i][0]
            times = c[i][1]
            if ans == "" and key == "0":
                break
            ans += key * (times // 2)
            c[i][1] = times % 2
        
        for i in range(len(c)):
            if c[i][1]:
                ans = ans + c[i][0] + ans[::-1]
                return ans
        return ans + ans[::-1]

t = Solution()
print(t.largestPalindromic(num = "22"))

            