class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        line_board = []
        size = len(board)
        visited = [0] * size * size

        for i in range(0, size):
            for j in range(0, size):
                ii = size - 1 - i
                jj = j
                if i % 2 == 1:
                    jj = size - 1 - j
                line_board.append(board[ii][jj])
        for i in range(1, size * size + 1):
            print(i, line_board[i - 1])
        queue = []
        visited[0] = 1
        queue.append((0, 0))

        while queue:
            index, step = queue.pop(0)
            for i in range(1, 7):
                nextindex = index + i
                if nextindex >= size * size:
                    continue
                if visited[nextindex]:
                    continue
                if nextindex == size * size - 1:
                    return step + 1
                visited[nextindex] = 1
                target = line_board[nextindex]
                if target != -1 and not visited[target - 1]:
                    target -= 1
                    if target == size * size - 1:
                        return step + 1
                    visited[target] = 1
                    queue.append((target, step + 1))
                if target == -1:
                    queue.append((nextindex, step + 1))

        return -1

board = [[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]
test = Solution()
print(test.snakesAndLadders(board))