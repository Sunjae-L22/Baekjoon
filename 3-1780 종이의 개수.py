# 1780번 종이의 개수
# 분할 정복, 재귀
import sys
N = int(input())

# paper[x][y]는 x행 y열을 의미
paper = [[0] * N for i in range(N)]
n_of_paper = [0, 0, 0]
for i in range(N):
    paper[i] = list(map(int, sys.stdin.readline().split()))


# 지금 종이가 모두 같은 수로 되어있는지 판별하는 함수
def is_it_same(r, c, n):
    tmp = paper[r][c]
    for i in range(n):
        for j in range(n):
            # 모든 수가 같지 않다? -> 그 순간 9분할!
            if tmp != paper[r+i][c+j]:
                n //= 3
                is_it_same(r, c, n)
                is_it_same(r, c+n, n)
                is_it_same(r, c+2*n, n)
                is_it_same(r+n, c, n)
                is_it_same(r+n, c+n, n)
                is_it_same(r+n, c+2*n, n)
                is_it_same(r+2*n, c, n)
                is_it_same(r+2*n, c+n, n)
                is_it_same(r+2*n, c+2*n, n)
                return

    # 위의 for 문을 통과했다는건 모든 수가 같다는것
    if tmp == -1:
        n_of_paper[0] += 1
    elif tmp == 0:
        n_of_paper[1] += 1
    else:
        n_of_paper[2] += 1


is_it_same(0, 0, N)
for i in n_of_paper:
    print(i, sep='\n')