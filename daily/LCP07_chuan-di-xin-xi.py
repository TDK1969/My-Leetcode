class Solution:
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

