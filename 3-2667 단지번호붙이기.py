# 2667번 단지번호붙이기
# 너비 우선 탐색(BFS), 깊이 우선 탐색(DFS)
import sys
from collections import deque
N = int(input())
apart = [[0]*N for _ in range(N)]
for t in range(N):
    apart[t] = list(map(int, sys.stdin.readline().rstrip()))

# 상하좌우 움직임
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

# 단지내 집 수를 저장할 list
houses = []


def bfs(n, a, b):
    q = deque()
    q.append((a, b))
    apart[a][b] = 0
    n_house = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            # 범위 넘어가면 pass
            if next_x < 0 or next_y < 0 or next_x > n-1 or next_y > n-1:
                continue
            if apart[next_x][next_y] == 1:
                n_house += 1
                apart[next_x][next_y] = 0
                q.append((next_x, next_y))
    return n_house


# 1이 나오는 점부터 bfs를 시작
for j in range(N):
    for k in range(N):
        if apart[j][k] == 1:
            houses.append(bfs(N, j, k))

houses.sort()
print(len(houses))
for n in houses:
    print(n)