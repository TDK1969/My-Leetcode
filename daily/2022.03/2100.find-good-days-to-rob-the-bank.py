from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        return [i for i in range(n) if left[i] >= time and right[i] >= time]

test = Solution()
print(test.goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))
