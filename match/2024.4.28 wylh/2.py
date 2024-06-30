import heapq
n, m = map(int, input().split())
tasks = []
for _ in range(n):
    tasks.append(list(map(int, input().split())))

tickets = []
for _ in range(m):
    if len(tickets) == 0:
        tickets.append(int(input()))
    else:
        tickets.append(tickets[-1] + int(input()))

tasks.sort(key=lambda x:x[1])
def solution(tasks: List[int], tickets: List[int]) -> int:
    h = []
    heapq.heapify(h)
    # h中最多有m个

    def push(value: int, size: int):
        if len(h) < size:
            heapq.heappush(h, value)
        else:
            if value > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, value)

    for value, limit in tasks:
        if (tickets[limit - 1] if limit - 1 < len(tickets) else tickets[-1]) == 0:
            continue
        push(value, tickets[limit - 1] if limit - 1 < len(tickets) else tickets[-1])
    
    return sum(h)
print(solution(tasks, tickets))
