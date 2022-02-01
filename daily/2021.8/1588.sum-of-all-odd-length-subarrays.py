from typing import List


class Solution:
    def sum0ddLengthSubarrays(self, arr: List[int]) -> int:
        presums = [0]
        presum = 0
        for num in arr:
            presum += num
            presums.append(presum)
        n = len(arr)
        max_len = n if n & 1 else n - 1
        ans = 0
        for i in range(1, max_len + 1, 2):
            for start in range(0, len(presums) - i):
                ans += presums[start + i] - presums[start]
        return ans

test = Solution()
print(test.sum0ddLengthSubarrays([1]))