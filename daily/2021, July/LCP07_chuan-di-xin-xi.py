class Solution1:
    """
    BFS
    """
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        queue = []
        queue.append((0, 0))
        count = 0

        while queue:
            temp, round = queue.pop(0)
            if round == k and temp == n - 1:
                count += 1
            if round < k:
                for way in relation:
                    if way[0] == temp:
                        queue.append((way[1], round + 1))

        return count


class Solution:
    """
    dp
    """
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [[0 for i in range(n)] for j in range(k + 1)]
        dp[0][0] = 1

        for i in range(1, k + 1):
            for way in relation:
                dp[i][way[1]] += dp[i - 1][way[0]]

        return dp[k][n - 1]