from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans = []

        if intLength == 1:
            for i in queries:
                ans.append(i - 1)

            return ans
        elif intLength == 2:
            for i in queries:
                ans.append(11 * i)

            return ans
        else:
            for i in queries:
                temp = 0
                l = 0 if intLength & 1 == 1 else 1
                while i > 10:
                    n = i % 10
                    temp += (10 ** l + 1) * ((n - 1) % 10)
                    i = i // 10
                    l += 2
                temp += (10 ** l + 1) * i
                ans.append(temp)
            return ans

test = Solution()
print(test.kthPalindrome([1,2,3,4,5,90], 3))

                


            