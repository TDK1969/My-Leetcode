class Solution:
    def nearestExit(self, maze, entrance) -> int:
        wayout = set()
        row = len(maze)
        col = len(maze[0])
        visited = [[0 for i in range(col)] for j in range(row)]

        for x in range(0, row):
            if maze[x][0] == '.':
                wayout.add((x, 0))
            if maze[x][col - 1] == '.':
                wayout.add((x, col - 1))
        for y in range(0, col):
            if maze[0][y] == '.':
                wayout.add((0, y))
            if maze[row - 1][y] == '.':
                wayout.add((row - 1, y))

        if (entrance[0], entrance[1]) in wayout:
            wayout.remove((entrance[0], entrance[1]))

        queue = []
        queue.append(((entrance[0], entrance[1]), 0))
        visited[entrance[0]][entrance[1]] = 1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while queue:
            temp, step = queue.pop(0)
            if temp in wayout:
                return step

            for move_x, move_y in directions:
                next_x = temp[0] + move_x
                next_y = temp[1] + move_y
                if 0 <= next_x < row and 0 <= next_y < col:
                    if maze[next_x][next_y] == '.' and not visited[next_x][next_y]:
                        if (next_x, next_y) in wayout:
                            return step + 1
                        visited[next_x][next_y] = 1
                        queue.append(((next_x, next_y), step + 1))

        return -1

test = Solution()
print(test.nearestExit([[".","+"]], [0,0]))