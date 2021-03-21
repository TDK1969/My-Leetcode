class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a = len(matrix)
        b = len(matrix[0])
        row = [0] * a
        col = [0] * b

        for i in range(0, a):
            for j in range(0, b):
                if matrix[i][j] == 0 and (row[i] == 0 or col[j] == 0):
                    for y in range(0, b):
                        if matrix[i][y]:
                            matrix[i][y] = None
                    for x in range(0, a):
                        if matrix[x][j]:
                            matrix[x][j] = None
                    row[i] = 1
                    col[j] = 1

        for i in range(0, a):
            for j in range(0, b):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix):
        # 用矩阵中的第0行和第0列来标记，不需要使用额外空间
        m = len(matrix)
        n = len(matrix[0])

        col0_haszero = any(matrix[i][0] == 0 for i in range(m))
        row0_haszero = any(matrix[0][j] == 0 for j in range(n))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col0_haszero:
            for i in range(m):
                matrix[i][0] = 0

        if row0_haszero:
            for j in range(n):
                matrix[0][j] = 0
