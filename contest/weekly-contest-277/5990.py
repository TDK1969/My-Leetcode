from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans = []
        temp = []
        count = set()
        numbers = Counter(nums)

        for i in nums:
            if i not in count:
                temp.append(i)
            count.add(i)

        for i in temp:
            if i - 1 not in count and i + 1 not in count and numbers[i] == 1:
                ans.append(i)

        return ans
