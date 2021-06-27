class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        line_board = []
        size = len(board)
        visited = [0] * size * size
        print(visited)
        for i in range(0, size):
            for j in range(0, size):
                ii = size - 1 - i
                jj = j
                if i % 2 == 1:
                    jj = size - 1 - j
                line_board.append(board[ii][jj])

        print(line_board)
        queue = []
        visited[0] = 1
        queue.append((0, 0))

        while queue:
            index, step = queue.pop(0)
            print(index, step)
            for i in range(1, 6):
                nextindex = index + 1
                if not visited[nextindex]:
                    continue
                if nextindex == size * size - 1:
                    return step + 1
                target = line_board[nextindex]
                if target != -1 and not visited[target]:
                    if target == size * size - 1:
                        return step + 1
                    queue.append((target, step + 1))
            if not visited[index + 6]:
                visited[index + 6] = 1
                queue.append((index + 6, step + 1))

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]        
test = Solution()
print(test.snakesAndLadders(board))