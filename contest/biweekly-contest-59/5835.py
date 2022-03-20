from typing import List
import heapq

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        sum = 0
        count = 0
        min_num = float("inf")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sum += abs(matrix[i][j])
                min_num = min(min_num, abs(matrix[i][j]))
                if matrix[i][j] <= 0:
                    count += 1
        if count & 1:
            sum -= 2 * min_num

        return sum

test = Solution()
print(test.maxMatrixSum([[2,9,3],[5,4,-4],[1,7,1]]))
