from typing import List
from math import log

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        layer = int(log(label, 2))
        ans = []
        temp = label
        while layer >= 1:
            ans.append(temp)
            temp = 2**layer + 2**(layer - 1) - 1 - temp // 2
            layer -= 1
        ans.append(1)
        ans.reverse()
        return ans

test = Solution()
print(test.pathInZigZagTree(14))