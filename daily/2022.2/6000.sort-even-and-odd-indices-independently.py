from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = []
        even = []
        for i, num in enumerate(nums):
            if i & 1:
                odd.append(num)
            else:
                even.append(num)
        odd.sort(reverse=True)
        even.sort(reverse=False)

        ans = []
        for i in range(0, n, 2):
            ans.append(even[i // 2])
            if i // 2 < len(odd):
                ans.append(odd[i // 2])

        return ans

