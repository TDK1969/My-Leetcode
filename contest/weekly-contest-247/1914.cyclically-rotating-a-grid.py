class Solution:
    def rotateGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        term = min(m, n) // 2

        for i in range(term):
            linar = []
            for j in range(i, n - i):
                linar.append(grid[i][j])
            linar.pop()
            for p in range(i, m - i):
                linar.append(grid[p][n - i - 1])
            linar.pop()
            for j in range(n - i - 1, i - 1, -1):
                linar.append(grid[m - i - 1][j])
            linar.pop()
            for p in range(m - i - 1, i - 1 , -1):
                linar.append(grid[p][i])
            linar.pop()

            kk = k
            k = k % len(linar)
            for j in range(k):
                linar.append(linar.pop(0))
            k = kk

            for j in range(i, n - i):
                grid[i][j] = linar.pop(0)
            for p in range(i, m - i):
                if p == i:
                    continue
                grid[p][n - i - 1] = linar.pop(0)
            for j in range(n - i - 1, i - 1, -1):
                if j == n - i - 1:
                    continue
                grid[m - i - 1][j] = linar.pop(0)
            for p in range(m - i - 1, i - 1 , -1):
                if p == m - i - 1 or p == i:
                    continue
                grid[p][i] = linar.pop(0)

        return grid

test = Solution()
print(test.rotateGrid([[40,10],[30,20]], 1))