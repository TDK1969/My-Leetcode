from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indexs = []
        for index, val in enumerate(nums):
            if val == key:
                indexs.append(index)

        ans = set()
        for index in indexs:
            for j in range(-k, k + 1):
                if 0 <= index + j < len(nums):
                    ans.add(index + j)
        return list(ans)

test = Solution()
print(test.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))