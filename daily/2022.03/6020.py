from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numsCount = {}
        for num in nums:
            if num not in numsCount:
                numsCount[num] = 1
            else:
                numsCount[num] += 1

        for num in numsCount:
            if numsCount[num] & 1:
                return False
        return True