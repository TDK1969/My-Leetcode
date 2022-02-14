from typing import List
from collections import defaultdict


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        idx = 0
        maxTime = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            curTime = releaseTimes[i] - releaseTimes[i - 1]
            if curTime > maxTime:
                idx, maxTime = i, curTime
            elif curTime == maxTime and ord(keysPressed[idx]) < ord(keysPressed[i]):
                idx = i

        return keysPressed[idx]

test = Solution()
print(test.slowestKey([19,22,28,29,66,81,93,97], "fnfaaxha"))


