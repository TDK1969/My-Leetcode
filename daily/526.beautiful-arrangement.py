class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        match = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)
        visited = set()

        def back_track(index):
            if index == n + 1:
                nonlocal count
                count += 1
                return
            for num in match[index]:
                if num not in visited:
                    visited.add(num)
                    back_track(index + 1)
                    visited.remove(num)

        back_track(1)
        return count

test = Solution()
print(test.countArrangement(3))



