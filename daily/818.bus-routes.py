class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        
        visited = [0] * len(routes)
        mapstop = {}
        for i in range(len(routes)):
            keys = mapstop.keys()
            for stop in routes[i]:
                if stop not in keys:
                    mapstop[stop] = []
                mapstop[stop].append(i)

        queue = []
        for i in mapstop[source]:
            visited[i] = 1
            queue.append((i, 1))

        while queue:
            route_index, times = queue.pop(0)
            if target in routes[route_index]:
                return times
            for stop in routes[route_index]:
                for line in mapstop[stop]:
                    if not visited[line]:
                        visited[line] = 1
                        queue.append((line, times+1))

        return -1


test = Solution()
routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
print(test.numBusesToDestination(routes, 15, 12))