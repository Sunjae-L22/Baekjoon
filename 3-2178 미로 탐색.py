# 2178번 미로 탐색
# 너비 우선 탐색(BFS)
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
maze = [[0] * M for _ in range(N)]

for i in range(N):
    maze[i] = list(map(int, sys.stdin.readline().strip()))

# 최단거리 저장 - 처음도 포함하기 때문에 dis[n][m] = 1
dis = [[0] * M for _ in range(N)]
dis[0][0] = 1


def bfs(n, m):
    q = deque()
    q.append((n, m))
    # 상하좌우 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        # 다음 이동 방향 설정
        for j in range(4):
            next_x = x + dx[j]
            next_y = y + dy[j]
            # 0이면 안 가고 1이면 가, 범위 안에서만 이동
            if next_x < 0 or next_x > N-1 or next_y < 0 or next_y > M-1:
                continue
            if maze[next_x][next_y] == 0:
                continue
            if maze[next_x][next_y] == 1 and dis[next_x][next_y] == 0:
                dis[next_x][next_y] = dis[x][y] + 1
                q.append((next_x, next_y))
    return dis[N-1][M-1]


print(bfs(0, 0))