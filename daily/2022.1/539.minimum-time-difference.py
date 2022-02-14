from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:  # 通过鸽巢原理提高效率
            return 0

        minDiff = float("inf")

        times = []
        for i in timePoints:
            times.append((int(i.split(":")[0]), int(i.split(":")[1])))
        times.sort()

        for i in range(0, len(times) - 1):
            diff = times[i + 1][0] * 60 + times[i + 1][1] - times[i][0] * 60 - times[i][1]
            minDiff = min(minDiff, diff)

        diff = 1440 - (times[-1][0] * 60 + times[-1][1] - times[0][0] * 60 - times[0][1])
        minDiff = min(minDiff, diff)

        return minDiff

test = Solution()
print(test.findMinDifference(["12:01","00:10","00:01"]))