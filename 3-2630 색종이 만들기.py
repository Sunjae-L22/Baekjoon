# 2630번 색종이
# 분할 정복
import sys
N = int(input())
color = [[0] * N for _ in range(N)]
for _ in range(N):
    color[_] = list(map(int, sys.stdin.readline().split()))

colors = [0, 0]


def paper(x, y, n):
    tmp = color[x][y]
    for i in range(n):
        for j in range(n):
            if tmp != color[x+i][y+j]:
                n = n // 2
                paper(x, y, n)
                paper(x, y+n, n)
                paper(x+n, y, n)
                paper(x+n, y+n, n)
                return
    if tmp == 0:
        colors[0] += 1
    elif tmp == 1:
        colors[1] += 1


paper(0, 0, N)
print(colors[0])
print(colors[1])