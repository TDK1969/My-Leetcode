class Solution:
    def eliminateMaximum(self, dist, speed):
        """

        :type dist: list
        :type speed: list
        :rtype: int
        """
        count = 0
        n = len(dist)
        for i in range(n):
            dist[i] = dist[i] / speed[i]

        dist.sort()
        for i in range(n):
            if i > dist[i]:
                return count
            count += 1

        return count

