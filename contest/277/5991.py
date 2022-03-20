from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plus = [i for i in nums if i > 0]
        minus = [i for i in nums if i < 0]
        ans = []
        for i in range(len(plus)):
            ans.append(plus[i])
            ans.append(minus[i])
        return ans