# 1992번 쿼드트리
# 분할 정복, 재귀
import sys
N = int(input())
list_0_1 = [[0] * N for _ in range(N)]

for i in range(N):
    list_0_1[i] = list(map(int, sys.stdin.readline().strip()))


def quadtree(x, y, n):
    tmp = list_0_1[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 4개로 나누어 압축하는 순간 괄호로 묶으므로 여기에 괄호 추가
            if tmp != list_0_1[i][j]:
                print('(', end='')
                n //= 2
                quadtree(x, y, n)
                quadtree(x, y + n, n)
                quadtree(x+n, y, n)
                quadtree(x+n, y+n, n)
                print(')', end='')
                return
    if tmp == 0:
        print('0', end='')
    elif tmp == 1:
        print('1', end='')


quadtree(0, 0, N)