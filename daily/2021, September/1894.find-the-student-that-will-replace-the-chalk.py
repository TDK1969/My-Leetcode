from itertools import accumulate
from typing import List
import bisect

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = list(accumulate(chalk))
        k %= chalk_sum[-1]
        return bisect.bisect_left(chalk_sum, k)



