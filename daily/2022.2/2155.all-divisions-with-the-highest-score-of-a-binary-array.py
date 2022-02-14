from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = []
        ones = []

        for num in nums:
            if num == 0:
                if not zeros:
                    zeros.append(1)
                else:
                    zeros.append(zeros[-1] + 1)
            else:
                if not zeros:
                    zeros.append(0)
                else:
                    zeros.append(zeros[-1])

        for num in nums[::-1]:
            if num == 1:
                if not ones:
                    ones.append(1)
                else:
                    ones.append(ones[-1] + 1)
            else:
                if not ones:
                    ones.append(0)
                else:
                    ones.append(ones[-1])

        ones.reverse()

        ans = []
        maxpoint = 0
        zeros.insert(0, 0)
        ones.append(0)

        for i in range(n + 1):
            if zeros[i] + ones[i] > maxpoint:
                maxpoint = zeros[i] + ones[i]
                ans = [i]
            elif zeros[i] + ones[i] == maxpoint:
                ans.append(i)

        return ans

test = Solution()
print(test.maxScoreIndices([0,0,1,0]))

