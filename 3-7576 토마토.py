# 7576번 토마토
# 너비 우선 탐색(BFS)
import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
tomato_box = [[0] * M for i in range(N)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
day = 0
# 큐에 익은 토마토 저장
q = deque()

# 토마토 배열 입력
for i in range(N):
    tomato_box[i] = list(map(int, sys.stdin.readline().split()))
# 익은 모든 토마토의 위치를 큐에 저장
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and tomato_box[next_x][next_y] == 0:
                tomato_box[next_x][next_y] = tomato_box[x][y] + 1
                q.append([next_x, next_y])


bfs()
# 인접한 토마토가 다 익고도 0이 존재하면(안 익은 토마토가 존재하면) -1 출력
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            print(-1)
            exit(0)
        else:
            day = max(day, tomato_box[i][j])
print(day-1)