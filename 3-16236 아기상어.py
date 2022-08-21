# 16236번 아기상어
#

import sys
from collections import deque
N = int(input())
space = [[0]*N for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
# 아기상어의 크기
shark_loc_x = 0
shark_loc_y = 0
baby_shark = 2

# 물고기 배열 입력
for i in range(N):
    space[i] = list(map(int, sys.stdin.readline().split()))
# 상어 위치 탐색
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_loc_x = i
            shark_loc_y = j


def bfs(x, y, baby_shark_size):
    dist = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    fish_eat = []

    while q:
        loc_x, loc_y = q.popleft()
        for i in range(4):
            next_x = loc_x + dx[i]
            next_y = loc_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == 0:
                # 아기상어 크기가 물고기보다 크거나 같으면 지나갈 수 있음
                if baby_shark_size >= space[next_x][next_y]:
                    q.append([next_x, next_y])
                    visited[next_x][next_y] = 1
                    dist[next_x][next_y] = dist[loc_x][loc_y] + 1
                    # 아기상어 크기가 물고기보다 크면 먹을 수 있음, fish_eat[]에 저장
                    if (baby_shark_size > space[next_x][next_y]) and space[next_x][next_y] != 0:
                        fish_eat.append((next_x, next_y, dist[next_x][next_y]))

    # 먹을 물고기를 거리, 가장 위, 가장 왼쪽 순으로 정렬
    return sorted(fish_eat, key=lambda x: (-x[2], -x[0], -x[1]))


time = 0
cnt = 0
while True:
    # 먹을 수 있는 물고기
    ate_fish = bfs(shark_loc_x, shark_loc_y, baby_shark)
    if len(ate_fish) == 0:
        break
    nx, ny, distance = ate_fish.pop()
    time += distance
    space[shark_loc_x][shark_loc_y] = 0
    space[nx][ny] = 0

    shark_loc_x = nx
    shark_loc_y = ny
    cnt += 1
    if cnt == baby_shark:
        baby_shark += 1
        cnt = 0
print(time)