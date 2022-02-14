from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        if not citations[0]:
            return 0
        h = 0
        for i in range(0, len(citations)):
            if citations[i] >= i + 1:
                if i == len(citations) - 1:
                    return len(citations)
                if citations[i + 1] <= i + 1:
                    return i + 1

test = Solution()
print(test.hIndex([3,3,3]))

