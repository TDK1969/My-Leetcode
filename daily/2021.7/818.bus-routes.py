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
        maproute = []
        for i in range(len(routes)):
            maproute.append([])
            keys = mapstop.keys()
            for stop in routes[i]:
                if stop not in keys:
                    mapstop[stop] = []
                mapstop[stop].append(i)

        if not mapstop.get(target):
            return -1
        end = mapstop[target]

        for i in range(len(routes)):
            for stop in routes[i]:
                maproute[i].extend(mapstop[stop])
                maproute[i] = list(set(maproute[i]))
            maproute[i].remove(i)

        queue = []
        for i in mapstop[source]:
            visited[i] = 1
            queue.append((i, 1))

        while queue:
            route_index, times = queue.pop(0)

            if route_index in end:
                return times

            for line in maproute[route_index]:
                if not visited[line]:
                    visited[line] = 1
                    queue.append((line, times + 1))
        return -1