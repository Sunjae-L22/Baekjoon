import sys
from collections import deque
X, Y = map(int, sys.stdin.readline().split())


def bfs(x, y):
    q = deque()
    q.append(x)
    while q:
        tmp = q.popleft()
        if tmp == y:
            print(dist[tmp])
            break
        for i in (tmp-1, tmp+1, tmp*2):
            # 안 들렀던 곳만 q 에다가 추가
            if (0 <= i <= 100000) and dist[i] == 0:
                dist[i] = dist[tmp] + 1
                q.append(i)


dist = [0 for _ in range(100001)]
bfs(X, Y)