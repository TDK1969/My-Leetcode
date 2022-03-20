from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        num = 0
        temp = 0
        n = len(rungs)
        i = 0
        while i < n:
            if temp + dist < rungs[i]:
                times = (rungs[i] - temp) // dist
                if (rungs[i] - temp) % dist == 0:
                    times -= 1
                temp += times * dist
                num += times
            else:
                temp = rungs[i]
                i += 1

        return num

test = Solution()
print(test.addRungs([1,3,5,10], 2))
