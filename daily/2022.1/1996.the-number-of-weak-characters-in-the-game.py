from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0
        index = 0
        n = len(properties)

        while index != n:
            temp = properties[index]
            if not stack:
                stack.append(temp)
                index += 1
            else:
                top = stack[-1]
                if temp[0] > top[0] and temp[1] > top[1]:
                    ans += 1
                    stack.pop()
                else:
                    stack.append(temp)
                    index += 1

        return ans

test = Solution()
print(test.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))

