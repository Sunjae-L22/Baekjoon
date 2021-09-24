import sys
from collections import deque

node, edge, start = map(int, sys.stdin.readline().split())

graph = [[0] * (node+1) for i in range(node+1)]
through = [0] * (node+1)

for _ in range(edge):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1


def dfs(st):
    through[st] = 1
    print(st, end=' ')
    for i in range(1, node+1):
        if graph[st][i] == 1 and through[i] == 0:
            dfs(i)


def bfs(st):
    queue = deque()
    queue.append(st)
    through[st] = 1
    while queue:
        st = queue.popleft()
        print(st, end=' ')
        for i in range(1, node+1):
            if graph[st][i] == 1 and through[i] == 0:
                queue.append(i)
                through[i] = 1


dfs(start)
through = [0] * (node+1)
print()
bfs(start)