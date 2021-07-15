from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix))]

        for i in range(len(matrix)):
            summ = 0
            for j in range(len(matrix[0])):
                summ += matrix[i][j]
                self.presum[i][j + 1] = summ

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix_sum = 0
        for i in range(row1, row2 + 1):
            matrix_sum += self.presum[i][col2 + 1] - self.presum[i][col1]
        return matrix_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
test = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
test.sumRegion(2,1,4,3)
