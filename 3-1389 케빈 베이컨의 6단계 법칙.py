import sys
from collections import deque

human, relation = map(int, sys.stdin.readline().split())
graph = [[0] * (human+1) for _ in range(human+1)]

for i in range(relation):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1


def bfs(start):
    through = [0] * (human + 1)
    n = [0] * (human+1)
    queue = deque()
    queue.append(start)
    through[start] = 1
    while queue:
        start = queue.popleft()
        for j in range(1, human+1):
            if graph[start][j] == 1 and through[j] == 0:
                n[j] = n[start] + 1
                queue.append(j)
                through[j] = 1
    return sum(n)


min_n = 1000000
min_human = 0

for i in range(1, human+1):
    if min_n > bfs(i):
        min_n = bfs(i)
        min_human = i
print(min_human)