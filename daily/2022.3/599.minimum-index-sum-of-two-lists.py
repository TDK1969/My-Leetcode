from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        m, n = len(list1), len(list2)
        minIndex = m + n

        for i in range(m):
            for j in range(n):
                if list1[i] == list2[j]:
                    if i + j < minIndex:
                        minIndex = i + j
                        ans = [list1[i]]
                    elif i + j == minIndex:
                        ans.append(list1[i])

        return ans

test = Solution()
print(test.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
