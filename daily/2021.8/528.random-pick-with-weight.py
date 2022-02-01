from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.presums = [0]
        presum = 0
        for num in w:
            presum += num
            self.presums.append(presum)

    def pickIndex(self) -> int:
        pick = random.randint(1, self.presums[-1])
        index = bisect.bisect_left(self.presums, pick) - 1
        return index


test = Solution([1])
print(test.pickIndex())
print(test.pickIndex())

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
